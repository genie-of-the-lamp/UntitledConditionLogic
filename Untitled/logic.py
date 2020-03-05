from . import Option
from collections import defaultdict
import re

class Logic(object):
    def __init__(self, option_data=[]):
        self._options = defaultdict(Option)
        self.selected_options = []
        self.enabled = set()
        self.disabled = set()

        if option_data:
            self.load_option_data(option_data)

    def load_option_data(self, option_data):
        for data in option_data:
            option = self.create_option(data.get("name"), optional=data.get("optional"))
            if data.get("children"):
                option._child_options.extend(data.get("children"))
            if data.get("incompatible"):
                option._incompatible_options.extend(data.get("incompatible"))

    def get_option(self, id):
        if id in self._options:
            option = self._options.get(id)
        else:
            option = self.create_option("NewOption")
        return option

    def create_option(self, name, optional=False):
        id = 0
        if self._options:
            id = max(self._options.keys())+1
        result = self.find_option_by_name(name, ambiguous=True)
        if result:
            exist_name = result[0]
            numbering = exist_name == name and 1 or int( exist_name[len(name):] )+1
            name = "{}{}".format(name, numbering)
        self._options[id] = Option(id, name, optional=optional)
        if not optional:
            self.enabled.add(id)

        return self._options.get(id)

    def find_option_by_name(self, name, ambiguous=False):
        suffix = ""
        matched = []
        if ambiguous:
            suffix="[0-9]*"
        for option in self._options.values():
            regex = re.compile(r"^{}{}$".format(name, suffix))
            mo = regex.match(option.name())
            if mo:
                matched.append((mo.group(), option))

        if not matched:
            return None

        if ambiguous:
            if len(matched) > 1:
                return max(matched, key=lambda x: x[0])

        return matched[0]

    def calculate(self, added_selection=None):
        if added_selection:
            unexist = [option for option in added_selection if option not in self.selected_options]
            if unexist:
                self.selected_options.extend(unexist)

        selected_options = self.selected_options
        for option_id in selected_options:
            option = self.get_option(option_id)
            self.enabled.update(set(option.children()))
            self.disabled.update(set(option.incompatible()))
        self.enabled.difference_update(self.disabled, self.selected_options)

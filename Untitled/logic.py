from . import Option
from collections import defaultdict
import re

class Logic(object):
    def __init__(self, option_data=[]):
        self._options = defaultdict(Option)
        self.selected_option_ids = set()
        self.enabled_option = set()
        self.disabled_option = set()

        if option_data:
            self.load_option_data(option_data)

    def load_option_data(self, option_data):
        temp_option_data = {
            "children": {},
            "incompatible": {},
        }
        for data in option_data:
            option = self.create_option(data.get("name"), optional=data.get("optional"))
            if data.get("children"):
                temp_option_data["children"][option.id()] = data.get("children")
            if data.get("incompatible"):
                temp_option_data["incompatible"][option.id()] = data.get("incompatible")

        for option_id, child_names in temp_option_data["children"].items():
            option = self.get_option(option_id)
            while child_names:
                child_name = child_names.pop()
                _, child = self.find_option_by_name(child_name)
                option.add_child(child)

        for option_id, incomp_names in temp_option_data["incompatible"].items():
            option = self.get_option(option_id)
            while incomp_names:
                incomp_name = incomp_names.pop()
                _, incomp = self.find_option_by_name(incomp_name)
                option.add_incompatible(incomp)

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
        option = Option(id, name, optional=optional)
        self._options[id] = option
        if not optional:
            self.enabled_option.add(option)

        return option

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
            self.selected_option_ids.update(added_selection)

        selected_options = self.selected_option_ids
        for option_id in selected_options:
            option = self.get_option(option_id)
            if option in self.enabled_option:
                self.enabled_option.remove(option)
            self.enabled_option.update(set(option.children()))
            self.disabled_option.update(set(option.incompatible()))
        self.enabled_option.difference_update(self.disabled_option)

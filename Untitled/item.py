from Untitled import *

class Condition(object):
    def __init__(self, combined=None, exclusive=None):
        self.option_set = {
        }
        if not combined:
            combined = []
        if not exclusive:
            exclusive = []
        self.option_set["combined"] = set(combined)
        self.option_set["exclusive"] = set(exclusive)


    def resolve(self, selected_options):
        selected = set(selected_options)
        combined = self.option_set["combined"]
        exclusive = self.option_set["exclusive"]
        if (selected.issuperset(combined) and not selected.intersection(exclusive)):
            return True
        return False


class ConditionedItem(object):
    def __init__(self, name):
        self.name = name
        self.conditions = []

    def reset_conditions(self):
        self.conditions.clear()

    def set_default(self):
        self.reset_conditions()
        self.add_condition()

    def add_condition(self, combined=None, exclusive=None):
        condition = Condition(combined, exclusive)
        self.conditions.append(condition)

    def item_resolve(self, selected_options):
        for condition in self.conditions:
            if condition.resolve(selected_options):
                return True
        return False

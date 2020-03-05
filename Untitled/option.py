class Option(object):
    def __init__(self, id, name, text="", children=None, incompatible=None, optional=False):
        self._id = id
        self._name = name
        self._text = text
        self._child_options = children
        if not self._child_options:
            self._child_options = []
        self._incompatible_options = incompatible
        if not self._incompatible_options:
            self._incompatible_options = []
        self.is_mandatory = not optional

    def id(self):
        return self._id

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        self.name()

    def text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        self.text()

    def children(self):
        return self._child_options

    def set_children(self, children):
        self._child_options = []
        for child in children:
            self.add_child(child)

    def add_child(self, child):
        if child not in self.children():
            self._child_options.append(child)

    def remove_child(self, child):
        if child in self._child_options:
            self._child_options.remove(child)
            return True
        return False

    def incompatible(self):
        return self._incompatible_options

    def set_incompatible(self, incompatible):
        self._incompatible_options = []
        for option in incompatible:
            self.add_incompatible(option)

    def add_incompatible(self, option):
        if option not in self.incompatible():
            self._incompatible_options.append(option)

    def remove_incompatible(self, option):
        if option in self._incompatible_options:
            self._incompatible_options.remove(option)
            return True
        return False



class CompositeOption(Option):
    """
    It is a combination of two or more options.
    This option not only receives children and incompatible options from parents,
    it can also have additional own things.
    """
    def __init__(self, id, name, parents, text="", children=None, incompatible=None):
        super().__init__(id, name, text, children, incompatible)
        self._parents = parents
        self.collision_check()

    def collision_check(self):
        old_children = set([child for parent in self._parents
                            for child in parent.children()])
        old_incomp_opts = set([option for parent in self._parents
                               for option in parent.incompatible()])
        parents_ids = set([parent.id() for parent in self._parents])
        # There are options that cannot be merged.
        if parents_ids.intersection(old_incomp_opts):
            # TODO: this error should be implement as new one.
            raise OptionMergeError

        old_incomp_opts.update(parents_ids)
        old_children.difference_update(old_incomp_opts)

        self.set_children(list(set(self.children()).union(old_children)))
        self.set_incompatible(list(set(self.incompatible()).union(old_incomp_opts)))


class OptionMergeError(Exception):
    """
    There are options that cannot be merged.
    """

class Option(object):
    """
    TODO: It should be possible to check if this option is Mandatory Option.
    """
    def __init__(self, id, name, text="", children=None, incompatible=None):
        self._id = id
        self._name = name
        self._text = text
        self._child_options = children
        if not self._child_options:
            self._child_options = []
        self._incompatible_options = incompatible
        if not self._incompatible_options:
            self._incompatible_options = []

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
        if child.id() not in self.children():
            self._child_options.append(child.id())

    def remove_child(self, child):
        if child.id() in self._child_options:
            del self._child_options[self._child_options.index(child.id())]
            return True
        return False

    def incompatible(self):
        return self._incompatible_options

    def set_incompatible(self, incompatible):
        self._incompatible_options = []
        for option in incompatible:
            self.add_incompatible(option)

    def add_incompatible(self, option):
        if option.id() not in self.incompatible():
            self._incompatible_options.append(option.id())

    def remove_incompatible(self, option):
        if option.id() in self._incompatible_options:
            del self._incompatible_options[self._incompatible_options.index(option.id())]
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

        if set([parent.id() for parent in self._parents]).intersection(old_incomp_opts):
            # TODO: this error should be implement as new one.
            raise ValueError

        old_children.difference_update(old_incomp_opts)
        self.set_children(list(set(self.children()).union(old_children)))

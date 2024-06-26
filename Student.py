from Human import Human
# from Group import Group
from typing import Any


class Student(Human):
    _class: Any

    def __init__(self, name, last_name, _id=None, group=None):
        super().__init__(name, last_name, _id)
        self._class = group

    def set_class(self, new_group):
        self._class = new_group

    def get_class(self):
        return self._class

    def __lt__(self, other: Human):
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name


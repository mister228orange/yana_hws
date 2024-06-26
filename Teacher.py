from typing import List, Any

from Discipline import Discipline
# from Group import Group
from Human import Human


class Teacher(Human):
    _homegroup: Any
    _disciplines: List[Discipline]

    def __init__(self, name: str, last_name: str, id=None, disciplines=None):
        super().__init__(name, last_name, id)
        self._disciplines = disciplines

    def set_homegroup(self, group):
        self._homegroup = group

    def get_homegroup(self):
        return self._homegroup

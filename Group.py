from enum import Enum
from Student import Student
from Teacher import Teacher

from typing import List


class Group(list):
    _grade: int
    _letter: str
    _students: List[Student]
    _homeroom_teacher: Teacher

    def __init__(self, teacher, students, grade=None, letter=None):
        super().__init__()
        self._students = sorted(students)
        self._homeroom_teacher = teacher
        teacher.set_homegroup(self)
        self._grade = grade
        self._letter = letter
        for i in range(len(self._students)):
            self._students[i].set_class(self)

    def __iter__(self):
        for x in list.__iter__(self):
            yield x

    def __getitem__(self, name):
        return [student for student in self._students
                if student.name.startswith(name) and student.last_name.startswith(name)]

s1 = Student('a', 'a')
s2 = Student('a', 'a')
t = Teacher('a', 'b')
g = Group(t, [s1, s2], 7, 'A')

pass
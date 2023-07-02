from person import Person
from gradesheet import GradeSheet


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self._grades = GradeSheet(self._personal_id, self.name)
        self.__class_room = None
        self._qualification = {}

    def get_detailed(self):
        return f"{super().get_details()}, class room: {self.__class_room}"

    @property
    def grades(self):
        return self._grades


    @property
    def personal_id(self):
        return self._personal_id

    @property
    def name(self):
        return self._name


    @property
    def class_room(self):
        return self.__class_room

    @class_room.setter
    def class_room(self, name):
        self.__class_room = name




from person import Person
from gradesheet import GradeSheet


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.grades = GradeSheet(self._personal_id, self.name)
        self._qualification = {}

    def get_detailed(self):
        return f"{super().get_details()}"

    @property
    def personal_id(self):
        return self.personal_id

    @property
    def name(self):
        return self._name










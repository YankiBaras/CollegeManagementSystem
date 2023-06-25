from person import Person


class Student(Person):
    def __init__(self, name, personal_id, classroom):
        super().__init__(name, personal_id)
        self._classroom = classroom
        self._courses = []
        self._grades = {}
        self._qualification = {}

    @property
    def classroom(self):
        return self._classroom

    @classroom.setter
    def classroom(self, value):
        self._classroom = value

    def get_detailed(self):
        return f"{super().get_details()}, Classroom: {self._classroom}, courses: {self._courses}"


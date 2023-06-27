from person import Person


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self._classroom = classroom
        self._courses = []
        self._grades = {}
        self._qualification = {}

    def get_detailed(self):
        return f"{super().get_details()}, classroom: {self._classroom}"


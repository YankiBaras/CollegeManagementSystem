from person import Person


class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, age, address)
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id

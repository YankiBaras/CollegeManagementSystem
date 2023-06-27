from person import Person


class Teacher(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self._course = course


    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value

    def get_details(self):
        return f"{super().get_details()}, course: {self._course}"



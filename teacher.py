from person import Person


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__course = None

    @property
    def name(self):
        return self._name

    @property
    def personal_id(self):
        return self._personal_id

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self,name):
        self.__course = name

    def get_details(self):
        return f"{super().get_details()}, course: {self.__course}"





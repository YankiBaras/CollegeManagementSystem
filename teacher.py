from person import Person


class Teacher(Person):
    def __init__(self, name, address, age, subject):
        super().__init__(name, age, address)
        self._subject = subject

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


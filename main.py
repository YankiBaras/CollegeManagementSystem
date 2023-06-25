class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, age, address)
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id


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


class Grade:
    def __init__(self, student, course, grade):
        self._student = student
        self._course = course
        self._grade = grade






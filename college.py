class College:

    def __init__(self, name):
        self.__name = name
        self.__students = []
        self.__teachers = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.__name = value

    def get_students(self):
        return self.__students

    def get_teachers(self):
        return self.__teachers

    def add_student(self,student):
        self.__students.append(student)

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def remove_student(self, student):
        self.__students.remove(student)

    def remove_teacher(self, teacher):
        self.__teachers.remove(teacher)


from teacher import Teacher
from teacher_manager import TeachersManager


class Course(TeachersManager):

    def __init__(self, course_name):
        super().__init__()
        self.__name = course_name
        self.__teacher = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def add_teacher(self, name):
        teacher = Teacher(name)
        teacher.course = self.__name
        self.__teacher = teacher
        self.collection.append(teacher)

    def get_teacher(self):
        return self.__teacher

    def get_teachers(self):
        teachers = []
        for teacher in self.collection:
            teachers.append(teacher.get_details())
        return teachers

    def get_teachers_instance(self):
        teachers = []
        for teacher in self.collection:
            teachers.append(teacher)
        return teachers












from teacher import Teacher
from collectionmanager import CollectionManager


class Course(CollectionManager):

    def __init__(self, course_name):
        super().__init__()
        self.__name = course_name
        self.__teachers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_teacher(self):
        teachers = []
        for teacher in self.__teachers:
            teachers.append(teacher.get_details())
        return teachers

    def add_teacher(self, name):
        self.__teachers.append(Teacher(name))










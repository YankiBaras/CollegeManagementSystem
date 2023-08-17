from teacher import Teacher
from collectionmanager import CollectionManager


class Course(CollectionManager):

    def __init__(self, name):
        super().__init__(name)
        self.__teacher = None

    def add_teacher(self, name):
        teacher = Teacher(name)
        teacher.course = self.name
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












import sqlite3
from teacher import Teacher
from collectionmanager import CollectionManager


class Course:

    def __init__(self, course_name):
        super().__init__()
        self.__name = course_name
        self.__teacher = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, name):
        self.__teacher.append(Teacher(name))








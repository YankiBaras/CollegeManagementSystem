import sqlite3

class Course:

    def __init__(self, course_name, course_subject):
        self.__course_name = course_name
        self.__course_subject = course_subject
        self.__teacher = None


    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, name):
        self.__course_name = name

    @property
    def course_subject(self):
        return self.__course_subject

    @course_subject.setter
    def course_subject(self, subject):
        self.__course_subject = subject


    @property
    def course_teacher(self):
        return self.__teacher

    @course_teacher.setter
    def course_teacher(self, teacher):
        self.__teacher = teacher






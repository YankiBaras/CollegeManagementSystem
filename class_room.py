from collectionmanager import CollectionManager
from student import Student
from course import Course


class ClassRoom(CollectionManager):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self.classroom_courses = []

    @property
    def name(self):
        return self._name

    def add_student(self, name):
        self.collection.append(Student(name))

    def add_course(self, course):
        self.classroom_courses.append(Course(course))

    def get_student(self, name):
        for i in self.collection:
            if i.name == name:
                return i

    def get_courses(self):
        courses = []
        for course in self.classroom_courses:
            courses.append(course.name)
        return courses


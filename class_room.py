from collectionmanager import CollectionManager
from student import Student
from course import Course


class ClassRoom(CollectionManager):
    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self.classroom_courses = []

    @property
    def name(self):
        return self._name

    def add_student(self, name):
        student = Student(name)
        student.class_room = self._name
        self.collection.append(student)

    def get_student(self, personal_id):
        for i in self.collection:
            if i.personal_id == personal_id:
                return i

    def get_student_name(self, name):
        for i in self.collection:
            if i.name == name:
                return i

    def add_course(self, name):
        course = Course(name)
        course._classroom = self._name
        self.classroom_courses.append(course)

    def get_course(self, course):
        for cou in self.classroom_courses:
            if cou.name == course:
                return cou

    def get_courses(self):
        courses = []
        for course in self.classroom_courses:
            courses.append(course)
        return courses


from collectionmanager import CollectionManager


class ClassRoom(CollectionManager):
    def __init__(self, name):
        super().__init__(name)
        self.classroom_courses = []

    def add_student(self, name):
        self.collection.append(Student(name))

    def add_course(self, course):
        self.classroom_courses.append(course)

    def print_courses(self):
        for course in self.classroom_courses:
            print(course.course_name)


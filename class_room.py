class ClassRoom:

    def __init__(self, id, course):
        self.__classroomID = id
        self.classroom_course = course
        self.__classroom_students = []
        self.__classroom_courses = []

    @property
    def class_student(self):
        for s in self.__classroom_students:
            return s.name

    @class_student.setter
    def class_student(self, student):
        self.__classroom_students.append(student)

    def add_course(self, course):
        self.__classroom_courses = course

    def get_courses(self):
        for course in self.__classroom_courses:
            return course


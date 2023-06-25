class Course:

    def __init__(self, ID, course_name, course_subject):
        self.ID = ID
        self.__course_name = course_name
        self.__course_subject = course_subject
        self.__course_students = []

    def add_student(self, student):
        self.__course_students.append(student)

    def remove_student(self, student):
        self.__course_students.remove(student)

    @property
    def course_name(self):
        return self.__course_name


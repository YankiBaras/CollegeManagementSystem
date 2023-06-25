class Course:

    def __init__(self, ID, course_name, course_teacher):
        self.ID = ID
        self.__course_name = course_name
        self.__course_teacher = course_teacher
        self.__course_students = []

    def add_student(self, student):
        self.__course_students.append(student)

    def remove_student(self, student):
        self.__course_students.remove(student)

    @property
    def course_name(self):
        return self.__course_name


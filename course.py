class Course:

    def __init__(self, ID, course_name, course_subject):
        self.ID = ID
        self.__course_name = course_name
        self.__course_subject = course_subject
        self.__course_students = []

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
    def course_students(self):
        return self.__course_students

    @course_students.setter
    def course_students(self, student):
        self.__course_students.append(student)

    def remove_student(self, student):
        self.__course_students.remove(student)

    @property
    def course_teacher(self):
        return self.__teacher

    @course_teacher.setter
    def course_teacher(self, teacher):
        if teacher.course == self.__course_name:
            self.__teacher = teacher
        else:
            print("No match")




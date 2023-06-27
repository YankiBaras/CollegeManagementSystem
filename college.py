class College:
    classrooms = {}

    def __init__(self, name):
        self.__name = name
        self.__students = []
        self.__teachers = []
        self.__classrooms = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, student):
        self.__students.append(student)

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, teacher):
        self.__teachers.append(teacher)

    def remove_student(self, student):
        self.__students.remove(student)

    def remove_teacher(self, teacher):
        self.__teachers.remove(teacher)

    def remove_classroom(self, classroom):
        self.__classrooms.remove(classroom)

    def get_class(self, personal_id):
        swapped_dict = {student: cls for cls, students in College.classrooms.items() for student in students}
        for student in swapped_dict:
            if student.personal_id == personal_id:
                return swapped_dict[student].name


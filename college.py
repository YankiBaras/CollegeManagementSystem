class College:

    def __init__(self, name):
        self.__name = name
        self.__students = []
        self.__teachers = []
        self.classrooms = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

    def get_class(self, personal_id):
        swapped_dict = {student: cls for cls, students in College.classrooms.items() for student in students}
        for student in swapped_dict:
            if student.personal_id == personal_id:
                return swapped_dict[student].name


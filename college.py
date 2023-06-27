from class_room import ClassRoom


class College:

    def __init__(self, name):
        self.__name = name
        self.classrooms = []
        self.student_of_classroom = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_classroom(self, name):
        self.classrooms.append(ClassRoom(name))
        self.student_of_classroom[ClassRoom(name)] = ClassRoom(name).collection

    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

    def get_class(self, personal_id):
        swapped_dict = {student: cls for cls, students in self.student_of_classroom.items() for student in students}
        for student in swapped_dict:
            if student.personal_id == personal_id:
                return swapped_dict[student].name



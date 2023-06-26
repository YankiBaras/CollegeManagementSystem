class ClassRoom:

    def __init__(self, id):
        self.__classroomID = id
        self.__class_room = []

    @property
    def class_student(self):
        for s in self.__class_room:
            return s

    @class_student.setter
    def class_student(self, student):
        self.__class_room.append(student)

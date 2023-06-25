class ClassRoom:

    def __init__(self):
        self.__class_room = []

    def add_student(self, student):
        self.__class_room.append(student)

    def remove_student(self, student):
        self.__class_room.remove(student)
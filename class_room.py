class ClassRoom:

    def __init__(self, id):
        self.__class_room = id
        self.__class_room = []

    def add_student(self, student):
        self.__class_room.append(student)

    def remove_student(self, student):
        self.__class_room.remove(student)

    @property
    def classroom_id(self):
        return self.__class_room
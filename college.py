from class_room import ClassRoom
from collectionmanager import CollectionManager
from teacher import Teacher
from student import Student


class College:

    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.classrooms = []
        self.teachers = []
        self.student_of_classroom = {}
        self.student_of_teachers = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_classroom(self, name):
        self.classrooms.append(ClassRoom(name))
        self.student_of_classroom[ClassRoom(name)] = ClassRoom(name).collection

    def get_classroom(self, classroom_name):
        for i in self.classrooms:
            if i.name == classroom_name:
                return i

    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

    def get_student_class(self, personal_id):
        swapped_dict = {student: cls for cls, students in self.student_of_classroom.items() for student in students}
        for student in swapped_dict:
            if student.personal_id == personal_id:
                return swapped_dict[student].name

    def get_courses(self, name):
        for cla in self.classrooms:
            if cla.get_student(name).name == name:
                return cla.get_courses()

    def get_teachers(self):
        teachers = []
        for cla in self.classrooms:
            for course in cla.get_courses:
                for elem in course.collection:
                    teachers.append((elem.get_details()))
        return teachers

    def get_students(self):
        students = []
        for cla in self.classrooms:
            for elem in cla.collection:
                students.append((elem.get_details()))
        return students

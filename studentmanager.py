from collectionmanager import CollectionManager
from student import Student
from person import Person


class  StudentsManager(CollectionManager):
    def __init__(self):
        super().__init__()

    def add(self, name, classroom):
        self.collection.append(Student(name, classroom))

    def print_all_students(self):
        for student in self.collection:
            print(student.get_detailed())



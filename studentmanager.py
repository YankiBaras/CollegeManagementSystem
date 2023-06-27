from collectionmanager import CollectionManager
from student import Student


class  StudentsManager(CollectionManager):
    def __init__(self):
        super().__init__()

    def add(self, name, classroom):
        self.collection.append(Student(name, classroom))




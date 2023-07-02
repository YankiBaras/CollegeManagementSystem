from collectionmanager import CollectionManager
from teacher import Teacher


class TeachersManager(CollectionManager):
    def __init__(self):
        super().__init__()

    def add(self, name):
        teacher = Teacher(name)
        self.collection.append(teacher)




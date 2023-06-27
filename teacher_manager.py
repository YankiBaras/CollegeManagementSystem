from collectionmanager import CollectionManager
from teacher import Teacher


class TeachersManager(CollectionManager):
    def __init__(self):
        super().__init__()

    def add(self, name, course):
        self.collection.append(Teacher(name, course))

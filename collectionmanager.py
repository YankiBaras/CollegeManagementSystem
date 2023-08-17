class CollectionManager:
    def __init__(self, name):
        self._name = name
        self.collection = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add(self, instance):
        self.collection.append(instance)


    def remove_by_id(self, personal_id):
        for item in self.collection:
            if item.personal_id == personal_id:
                self.collection.remove(item)

    def remove_by_name(self, name):
        for item in self.collection:
            if item.name == name:
                self.collection.remove(item)

    def print_collection(self):
        for instance in self.collection:
            print(instance.get_detailed())

    def get_collection(self):
        return self.collection

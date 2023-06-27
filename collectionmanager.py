class CollectionManager:
    def __init__(self):
        self.collection = []


    def add(self, name, email):
        pass

    def remove_instacne(self, personal_id):
        for item in self.collection:
            if item.personal_id == personal_id:
                self.collection.remove(item)

    def print_all_collections(self):
        for instance in self.collection:
            print(instance.name, instance.email)



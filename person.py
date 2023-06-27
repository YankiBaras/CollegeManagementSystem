class Person:
    id_auto_increment = 1

    def __init__(self, name):
        self._name = name
        self._personal_id = Person.id_auto_increment
        Person.id_auto_increment += 1


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def personal_id(self):
        return self._personal_id

    def get_details(self):
        return f"Name: {self._name}, Personal_id: {self._personal_id}"

class Person:
    def __init__(self, name, personal_id):
        self._name = name
        self._personal_id = personal_id

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
        return f"Name: {self._name}, Age: {self._personal_id}"
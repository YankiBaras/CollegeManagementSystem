class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

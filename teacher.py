from person import Person


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self.name

    @property
    def personal_id(self):
        return self.personal_id


    def get_details(self):
        return f"{super().get_details()}, course: {self._course}"




class Qualification:
    def __init__(self):
        self._qualified = {}

    def update_qualified(self, course, is_qualified):
        self._qualified[course] = is_qualified

    @property
    def qualified(self):
        return self._qualified



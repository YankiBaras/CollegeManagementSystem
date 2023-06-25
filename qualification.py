class Qualification:
    def __init__(self, student, teacher, subject, is_qualified=False):
        self._student = student
        self._teacher = teacher
        self._subject = subject
        self._is_qualified = is_qualified

    @property
    def is_qualified(self):
        return self._is_qualified
    
    @is_qualified.setter
    def is_qulified(self):
        self._is_qualified = True



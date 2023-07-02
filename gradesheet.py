class GradeSheet:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
        self._grades = {}

    def update_grade(self, course, grade):
        if course not in self._grades:
            self._grades[course] = grade

    @property
    def grades(self):
        return self._grades

    def get_detail_grades(self):
        return f"ID: {self.__student_id}, Name: {self.__student_name}, Grade Sheet: {self._grades}"

    def average(self):
        average = 0
        count = 0
        for grade in self.__grades.values():
            average += grade
            count += 1
        return f"the average of {self.__student_name} is {average / count}"



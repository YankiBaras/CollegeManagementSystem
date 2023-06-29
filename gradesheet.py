class GradeSheet:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__grades = {}

    def update_grade(self, course, grade):
        if course not in self.__grades:
            self.__grades[course] = grade

    def get_grades(self):
        return f'id: {self.__student_id}, name: {self.__student_name} {self.__grades}'

    def average(self):
        average = 0
        count = 0
        for grade in self.__grades.values():
            average += grade
            count += 1
        return f"the average of {self.__student_name} is {average / count}"



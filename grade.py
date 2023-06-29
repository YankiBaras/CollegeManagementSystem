import sqlite3


class Grade:
    students_grades = []

    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__grade = {}
        Grade.students_grades.append(self.__grade)

    def update_grade(self, grade, course):
        self.__grade[course] = grade

    def get_grades(self):
        return f'id: {self.__student_id}, name: {self.__student_name} {self.__grade}'

    def grades_average(self):
        average = 0
        count = 0
        for grade in self.__grade.values():
            average += grade
            count += 1

        return f"the average of {self.__student_name} is {average / count}"



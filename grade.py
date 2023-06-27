import sqlite3

class Grade:
    #con = sqlite3.connect("college.db")
    #college_details = con.cursor()
    #college_details.execute("CREATE TABLE IF NOT EXISTS grades(name, student_id, course, grade)")
    students_grades = []
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__grade = {'student_id': self.__student_id, 'name': self.__student_name}
        Grade.students_grades.append(self.__grade)

    def update_grade(self, grade, course):
        self.__grade[course] = grade

    def get_grades(self, student_id):
        for dic in Grade.students_grades:
            if dic['student_id'] == student_id:
                return dic
        return self.__grade

    def grades_average(self, student_id):
        average = 0
        count = 0
        for dic in Grade.students_grades:
            if dic['student_id'] == student_id:
                for grade in dic.values():
                    average += grade
                    count += 1
                break
        return f"the average of {dic} is {average / count}"



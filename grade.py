class Grade:
    students_grades = []
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__grade = {'student_id':self.__student_id, 'name': student_name}
        Grade.students_grades.append(self.__grade)

    def update_grade(self, grade, course):
        self.__grade[course] = grade

    def get_grades(self, student_id):
        for dic in Grade.students_grades:
            if dic['student_id'] == student_id:
                return dic
        return self.__grade



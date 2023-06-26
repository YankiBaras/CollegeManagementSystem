from student import Student
from teacher import Teacher
from grade import Grade
from person import Person
from college import College
from course import Course
from class_room import ClassRoom


def main():
    college = College('MeGo')

    class_room_A = ClassRoom('A')
    class_room_B = ClassRoom('B')

    college.classrooms = class_room_A
    college.classrooms = class_room_B

    student1 = Student('Moshe', 1, 'A')
    student2 = Student('Michael', 4, 'B')

    course1 = Course(1, 'java', ',Software')
    course2 = Course(2, 'statistics', 'math')

    course1.course_students = student1
    course2.course_students = student2

    teacher1 = Teacher('Hime', 2, 'math')
    teacher2 = Teacher('Ronen', 3, 'English')

    class_room_A.class_student = student1
    class_room_B.class_student = student2

    college.students = student1
    college.students = student2

    college.teachers = teacher1
    college.teachers = teacher2

    student1_grades = Grade(1, 'Moshe')
    student1_grades.update_grade(95, 'java')
    student2_grades = Grade(4, 'Michael')
    student2_grades.update_grade(80, 'statistics')

    print(student1_grades.get_grades(1))
    print(student2_grades.get_grades(4))
    






main()
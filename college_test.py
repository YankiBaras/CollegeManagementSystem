from student import Student
from teacher import Teacher
from grade import Grade
from person import Person
from college import College
from course import Course
from class_room import ClassRoom


def main():
    class_room_A = ClassRoom('A')
    student1 = Student('Moshe', 1, 'A')
    class_room_A.add_student(student1)
    college = College('MeGo')

    teacher1 = Teacher('Hime', 2, 'math')

    college.add_student(student1)
    college.add_teacher(teacher1)
    for i in college.get_teachers():
        print(i.get_details())



main()
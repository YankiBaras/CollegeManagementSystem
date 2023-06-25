from student import Student
from teacher import Teacher
from grade import Grade
from person import Person
from college import College
from course import Course
from class_room import ClassRoom


def main():
    college = College('MeGo')
    student1 = Student('Moshe', 1)
    teacher1 = Teacher('Hime', 'math')

    college.add_student(student1)
    college.add_teacher(teacher1)
    for i in college.get_students():
        print(i.name)



main()
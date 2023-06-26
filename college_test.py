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

    teacher1 = Teacher('Hime', 2, 'math')
    teacher2 = Teacher('Ronen', 3, 'English')

    class_room_A.class_student = student1
    class_room_B.class_student = student2

    college.students = student1
    college.students = student2

    college.teachers = teacher1
    college.teachers = teacher2

    print(class_room_A.class_student.name)
    print(class_room_A.class_student.personal_id)
    print(class_room_A.class_student.classroom)
    print(class_room_A.class_student.name)




main()
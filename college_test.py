from student import Student
from teacher import Teacher
from gradesheet import GradeSheet
from person import Person
from college import College
from course import Course
from class_room import ClassRoom
from collectionmanager import CollectionManager
from studentmanager import StudentsManager
from teacher_manager import TeachersManager


def main():

    college = College('MeGo')

    college.add_classroom('AA')
    college.add_classroom('BB')

    college.get_classroom('AA').add_student('moshe')
    college.get_classroom('AA').add_student('yakov')
    college.get_classroom('BB').add_student('israel')
    college.get_classroom('BB').add_student('yosi')

    college.get_classroom('AA').add_course('java')
    college.get_classroom('AA').add_course('python')
    college.get_classroom('BB').add_course('math')
    college.get_classroom('BB').add_course('english')

    college.get_classroom('AA').get_course('java').add_teacher('barak')
    college.get_classroom('AA').get_course('python').add_teacher('yoav')
    barak = college.get_classroom('AA').get_course('java').get_teacher()
    yoav = college.get_classroom('AA').get_course('python').get_teacher()

    moshe = college.get_classroom('AA').get_student('moshe')
    yakov = college.get_classroom('AA').get_student('yakov')

    moshe.grades.update_grade(86, 'java')
    moshe.grades.update_grade(70,'math')

    #college.get_classroom('AA').add_course('java')
    print(college.get_courses('moshe'))
    print(college.get_students())
    print(college.get_classroom('AA').get_course('java').get_teachers())
    print(college.get_teachers())
    print(moshe.class_room)
    print(college.is_teachers_student(6, 4))
    for course in college.get_classroom('AA').get_courses():
        print(course.name)

    print(college.get_teachers())
 
    teacher = Teacher('meni')
    teacher.course = 'math'
    print(teacher.course)
    moshe.qualified.update_qualified('math', 7)
    print(moshe.qualified.qualified)

main()

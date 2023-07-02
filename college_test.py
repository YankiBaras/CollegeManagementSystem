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
    college.get_classroom('AA').add_student('avi')
    college.get_classroom('AA').add_student('benni')


    college.get_classroom('BB').add_student('israel')
    college.get_classroom('BB').add_student('yosi')

    college.get_classroom('AA').add_course('java')
    college.get_classroom('AA').add_course('python')
    college.get_classroom('BB').add_course('math')
    college.get_classroom('BB').add_course('english')

    college.get_classroom('AA').get_course('java').add_teacher('barak')
    college.get_classroom('AA').get_course('python').add_teacher('yoav')

    moshe = college.get_classroom('AA').get_student_name('moshe')
    yakov = college.get_classroom('AA').get_student_name('yakov')
    avi = college.get_classroom('AA').get_student_name('avi')
    benni = college.get_classroom('AA').get_student_name('benni')

    moshe.grades.update_grade('java', 100)
    yakov.grades.update_grade('java', 100)
    avi.grades.update_grade('java', 80)
    benni.grades.update_grade('java', 86)

    moshe.grades.update_grade('math', 70)

    print(college.average_of_course('ab', 'AA'))

    # #college.get_classroom('AA').add_course('java')
    # print(college.get_courses('moshe'))
    # print(college.get_courses('avi'))
    # print(college.get_courses('benni'))
    # print(college.get_courses('yakov'))

    # print(college.get_students())
    # print(college.get_classroom('AA').get_course('java').get_teachers())
    # print(college.get_teachers())
    # print(moshe.class_room)
    # print(college.is_teachers_student(6, 4))


main()

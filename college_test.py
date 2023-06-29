from student import Student
from teacher import Teacher
from grade import Grade
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

    moshe = college.get_classroom('AA').get_student('moshe')
    yakov = college.get_classroom('AA').get_student('yakov')

    moshe.grade.update_grade(86, 'java')
    moshe.grade.update_grade(70,'python')

    #college.get_classroom('AA').add_course('java')
    print(college.get_courses('moshe'))
    print(college.get_students())
    #print(college.collection)


main()
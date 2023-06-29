class College:
    students = []

    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.classrooms = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_classroom(self, name):
        self.classrooms.append(ClassRoom(name))

    def get_classroom(self, classroom_name):
        for i in self.classrooms:
            if i.name == classroom_name:
                return i

    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

    def get_student_class(self, personal_id):
        swapped_dict = {student: cls for cls, students in self.student_of_classroom.items() for student in students}
        for student in swapped_dict:
            if student.personal_id == personal_id:
                return swapped_dict[student].name

    def get_courses(self, name):
        for cla in self.classrooms:
            if cla.get_student(name).name == name:
                return cla.get_courses()

    def get_teachers(self):
        teachers = []
        for cla in self.classrooms:
            for course in cla.get_courses:
                for elem in course.collection:
                    teachers.append((elem.get_details()))
        return teachers

    def get_students(self):
        students = []
        for cla in self.classrooms:
            for elem in cla.collection:
                students.append((elem.get_details()))
        return students


class CollectionManager:
    def __init__(self):
        self.collection = []

    def remove(self, personal_id):
        for item in self.collection:
            if item.personal_id == personal_id:
                self.collection.remove(item)

    def print_all_collections(self):
        for instance in self.collection:
            print(instance.get_detailed())

    def get_collection(self):
        return self.collection


class Course(CollectionManager):

    def __init__(self, course_name):
        super().__init__()
        self.__name = course_name
        self.__teacher = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher


class GradeSheet:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__grades = {}

    def update_grade(self, course, grade):
        if course not in self.__grades and course in College.get_student_class(self.__student_id).get_courses():
            self.__grades[course] = grade

    def get_grades(self):
        return f'id: {self.__student_id}, name: {self.__student_name} {self.__grades}'

    def average(self):
        average = 0
        count = 0
        for grade in self.__grades.values():
            average += grade
            count += 1
        return f"the average of {self.__student_name} is {average / count}"


class Person:
    id_auto_increment = 1

    def __init__(self, name):
        self._name = name
        self._personal_id = Person.id_auto_increment
        Person.id_auto_increment += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def personal_id(self):
        return self._personal_id

    def get_details(self):
        return f"Name: {self._name}, Personal_id: {self._personal_id}"


class Qualification:
    def __init__(self, student, teacher, subject, is_qualified=False):
        self._student = student
        self._teacher = teacher
        self._subject = subject
        self._is_qualified = is_qualified

    @property
    def is_qualified(self):
        return self._is_qualified

    def set_qualified(self):
        self._is_qualified = True


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.grades = GradeSheet(self._personal_id, self.name)
        self._qualification = {}
        College.students.append(self)

    def get_detailed(self):
        return f"{super().get_details()}"

    @property
    def personal_id(self):
        return self.personal_id

    @property
    def name(self):
        return self._name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def get_details(self):
        return f"{super().get_details()}"


class ClassRoom(CollectionManager):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self.classroom_courses = []

    @property
    def name(self):
        return self._name

    def add_student(self, name):
        self.collection.append(Student(name))

    def add_course(self, course):
        self.classroom_courses.append(Course(course))

    def get_student(self, name):
        for i in self.collection:
            if i.name == name:
                return i

    def get_courses(self):
        courses = []
        for course in self.classroom_courses:
            courses.append(course.name)
        return courses

def main():


    college = College('MeGo')
    mego_b = College('Mego2')
    mego_b.add_classroom('cc')
    mego_b.add_classroom('gg')
    mego_b.get_classroom('cc')

    college.add_classroom('AA')
    college.add_classroom('BB')

    college.get_classroom('AA').add_student('moshe')
    college.get_classroom('AA').add_student('yakov')
    college.get_classroom('BB').add_student('israel')
    college.get_classroom('BB').add_student('yosi')
    mego_b.get_classroom('gg').add_student('avi')
    mego_b.get_classroom('cc').add_student('Benni')
    mego_b.get_classroom('cc').add_course('OOP')
    mego_b.get_classroom('gg').add_course('algebra')
    mego_b.get_classroom('gg').add_course('OOP')

    # print(mego_b.get_classroom('gg').get_courses())


    college.get_classroom('AA').add_course('java')
    college.get_classroom('AA').add_course('python')
    college.get_classroom('AA').add_course('math')
    college.get_classroom('BB').add_course('english')
    college.get_classroom('AA').get_student('moshe').grades.update_grade('math', 98)

    moshe = college.get_classroom('AA').get_student('moshe')
    print(moshe.grades.get_grades())
    moshe.grades.update_grade('algebra', 96)
    moshe.grades.update_grade('python', 90)
    print(moshe.grades.average())

if __name__ == '__main__':
    main()








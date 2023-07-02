from class_room import ClassRoom


class College:

    def __init__(self, name):
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
        for classroom in self.classrooms:
            for student in classroom.collection:
                if student.personal_id == personal_id:
                    return classroom.name

    def get_courses(self, name):
        for cla in self.classrooms:
            if cla.get_student(name).name == name:
                courses = cla.get_courses()
                return set(list(course.name for course in courses))

    def get_teachers(self):
        teachers_ob = []
        for cla in self.classrooms:
            for course in cla.get_courses():
                for elem in course.get_teachers():
                    teachers_ob.append(elem)
        if len(teachers_ob) > 0:
            return teachers_ob
        return 'No teachers were found in the college'

    def get_students(self):
        students = []
        for cla in self.classrooms:
            for elem in cla.collection:
                students.append((elem.get_details()))
        return students

    def is_teachers_student(self, teacher_id, student_id):
        for course in self.get_classroom(self.get_student_class(student_id)).get_courses():
            for teacher in course.get_teachers_instance():
                if teacher.personal_id == teacher_id:
                    return True
        return False

    def average_of_course(self, course, name):
        len1 = 0
        sum1 = 0
        class_room = self.get_classroom(name)
        for stu in class_room.collection:
            if course in stu.grades.grades:
                len1 += 1
                sum1 += stu.grades.grades[course]
        try:
            return sum1 / len1
        except ZeroDivisionError:
            print("There isn't students in this course")



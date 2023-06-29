from class_room import ClassRoom



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
        self.student_of_classroom[ClassRoom(name)] = ClassRoom(name).collection

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
                return list(course.name for course in courses)

    def get_teachers(self):
        teachers = []
        for cla in self.classrooms:
            for course in cla.get_courses():
                if len(course.teacher) == 0:
                    return "No teachers were found in the college"
                else:
                    for elem in course.teacher:
                        teachers.append((elem.get_details()))
        return teachers

    def get_students(self):
        students = []
        for cla in self.classrooms:
            for elem in cla.collection:
                students.append((elem.get_details()))
        return students

    def is_teachers_student(self, teacher_id, student_id):
        for clas in self.classrooms:
            for course in self.get_student_class(student_id):
                return

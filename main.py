import sqlite3

con = sqlite3.connect("college.db")
college_details = con.cursor()

college_details.execute("CREATE TABLE students(name, student_id, course)")
college_details.execute("CREATE TABLE grades(name, student_id, course, grade)")
college_details.execute("""
 INSERT INTO students VALUES
        ('Moshe', 1, 'java'),
        ('michael', 4, 'statistics') 
""")

con.commit()
res = college_details.execute("SELECT course FROM students")
print(res.fetchall())

con.close()







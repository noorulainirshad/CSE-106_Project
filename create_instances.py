from backend import *

with app.app_context():

    #create student
    newUser = User(u_userId=1, u_userName='alonso', u_password='123')
    db.session.add(newUser)

    newStudent = Student(s_studentId=1, s_userId=1 ,s_name='Alonso')
    db.session.add(newStudent)

    #create teacher
    newUser = User(u_userId=2, u_userName='ammon', u_password='123')
    db.session.add(newUser)

    newTeacher = Teacher(t_teacherId=1, t_userId=2, t_name='Hepworth')
    db.session.add(newTeacher)

    #create class
    newClass = Class(c_classId=1, c_courseName='CSE-106', c_teacherId=1, c_enrollmentNum=0, c_capacity=4, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)

    db.session.commit()

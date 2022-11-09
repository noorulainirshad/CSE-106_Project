from backend import *

with app.app_context():

    #create student
    newUser = User(u_userId=1, u_userName='alonso', u_password='123')
    newUser2 = User(u_userId=2, u_userName='alexis', u_password='123')
    db.session.add(newUser)
    db.session.add(newUser2)

    newStudent = Student(s_studentId=1, s_userId=1 ,s_name='Alonso')
    newStudent2 = Student(s_studentId=2, s_userId=2 ,s_name='Alexis')
    db.session.add(newStudent)
    db.session.add(newStudent2)

    #create teacher
    newUser = User(u_userId=3, u_userName='ammon', u_password='123')
    db.session.add(newUser)

    newTeacher = Teacher(t_teacherId=1, t_userId=3, t_name='Hepworth')
    db.session.add(newTeacher)

    #create class
    newClass = Class(c_classId=1, c_courseName='CSE-106', c_teacherId=1, c_enrollmentNum=0, c_capacity=1, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)
    newClass = Class(c_classId=2, c_courseName='CSE-106-1', c_teacherId=1, c_enrollmentNum=0, c_capacity=4, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)
    newClass = Class(c_classId=3, c_courseName='CSE-106-2', c_teacherId=1, c_enrollmentNum=0, c_capacity=4, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)
    newClass = Class(c_classId=4, c_courseName='CSE-106-3', c_teacherId=1, c_enrollmentNum=0, c_capacity=4, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)

    db.session.commit()

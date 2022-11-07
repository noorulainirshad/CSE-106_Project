from backend import *

with app.app_context():
    newUser = User(u_userId=1, u_userName='alonso', u_password='123')
    db.session.add(newUser)

    newStudent = Student(s_studentId=1, s_userId=1 ,s_name='Alonso')
    db.session.add(newStudent)
    db.session.commit()
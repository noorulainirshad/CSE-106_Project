from backend import *

with app.app_context():
    newStudent = Student(s_studentId=1, s_userId=1 ,s_name='Alonso')
    db.session.add(newStudent)
    db.session.commit()
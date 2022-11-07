from backend import *

with app.app_context():
    newClass = Class(c_classId=1, c_courseName='CSE-106', c_teacherId=1, c_enrollmentNum=0, c_capacity=4, c_time='TR 5:00-7:00 PM')
    db.session.add(newClass)

    db.session.commit()
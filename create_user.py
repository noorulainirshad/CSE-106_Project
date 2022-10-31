from backend import *

with app.app_context():
    newUser = User(u_userId=1, u_userName='alonso', u_password='123')
    db.session.add(newUser)
    db.session.commit()
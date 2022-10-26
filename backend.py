from select import select
from flask import Flask, redirect, url_for
from flask import request
from flask import abort, render_template
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# choose where to store database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' 

# call database
db = SQLAlchemy(app)

# Student table with student name and grade
class Users(db.Model):
    u_userId = db.Column(db.Integer, primary_key=True)
    u_userName = db.Column(db.String, unique=True, nullable=False)
    u_password = db.Column(db.String, nullable=False)

class Teachers(db.Model):
    t_teacherId = db.Column(db.Integer, primary_key=True)
    t_userId = db.Column(db.Integer, unique=True, nullable=False)
    t_name = db.Column(db.String, nullable=False)

class Students(db.Model):
    s_studentId = db.Column(db.Integer, primary_key=True)
    s_userId = db.Column(db.Integer, nullable=False)
    s_name = db.Column(db.String, nullable=False)

class Classes(db.Model):
    c_classId = db.Column(db.Integer, primary_key=True)
    c_courseName = db.Column(db.String, unique=True, nullable=False)
    c_teacherId = db.Column(db.Integer, nullable=False)
    c_enrollmentNum = db.Column(db.Integer, nullable=False)
    c_capacity = db.Column(db.Integer, nullable=False)
    c_time = db.Column(db.DateTime, nullable=False)

class Enrollment(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    e_classId = db.Column(db.Integer, nullable=False)
    e_studentId = db.Column(db.Integer, nullable=False)
    e_grade = db.Column(db.Integer, nullable=False)


# root directory
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
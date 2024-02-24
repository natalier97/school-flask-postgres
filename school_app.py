from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

#creating an instance of Flask
school_app = Flask(__name__)

#configuring flask to use my betterschool database
school_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://natalie:1234@localhost/bestschool'


#initialize the sqlalchemy extension
db = SQLAlchemy(school_app)

#create a Model class for our tables
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.Integer, nullable=False)


class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.Integer, nullable=False)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)

@school_app.route('/')
def index():
    return "it is working"


#helper function for get_students()
def add_class_dict_to_json_students(json_teachers, json_students, json_subjects):
      for teacher in json_teachers:
        for student in json_students:
                if student['class']['subject'] == teacher['subject']:
                    student['class']['teacher'] = teacher['first_name']
                    for subject in json_subjects:
                         if subject['id'] == teacher['subject']:  
                            student['class']['subject'] = subject['subject']


#Returns a list of students along with their class names and the teacher of their class.
@school_app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    subjects = Subjects.query.all()
    teachers = Teachers.query.all()
    json_subjects = [{'id': subj.id, 'subject': subj.subject} for subj in subjects]

    json_teachers = [{'id': teacher.id, 'first_name': teacher.first_name, 'age': teacher.age,'subject': teacher.subject} for teacher in teachers]

    json_students = [{'id': stud.id, 'first_name': stud.first_name, 'last_name': stud.last_name, 'age': stud.age, "class":{"subject": stud.subject, 'teacher': '' } } for stud in students]

    add_class_dict_to_json_students(json_teachers, json_students, json_subjects)
                    

    response = jsonify(json_students)

    return response






school_app.run(debug=True)
from flask import render_template
from application.app import application
from application.schema import *

@application.route('/')
def root():
    return render_template('root.html')

@application.route('/students')
def student_list():
    all_students = Students.query.all()
    return render_template('all_students.html',list_of_names=all_students)

@application.route('/student/<int:id>')
def foreign_language(id):
    language_of_specific_student = Foreign_language.query.filter_by(student_id=id)
    student = Students.query.get(id)
    return render_template('languages.html',list_of_languages=language_of_specific_student,student=student)
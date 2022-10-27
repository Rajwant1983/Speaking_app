from application.app import d

class Students(d.Model):
    student_id = d.Column(d.Integer,nullable=False,primary_key=True)
    name = d.Column(d.String(100),nullable=False)
    email = d.Column(d.String(100),nullable=False)
    country = d.Column(d.String(100),nullable=False)
    native_language = d.Column(d.String(20),nullable=False)
    telephone = d.Column(d.Integer,nullable=False)
    foreign_language = d.relationship('Foreign_language')

class Foreign_language(d.Model):
    language_id = d.Column(d.Integer,nullable=False,primary_key=True)
    language_name = d.Column(d.String(100),nullable=False)
    student_id = d.Column(d.Integer,d.ForeignKey('students.student_id'),nullable=False)
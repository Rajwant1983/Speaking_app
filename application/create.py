# Perform static database operations
#
from schema import *

# Task -1 (only once)
# d.create_all()

# # Task - 2 (only once)
# c1 = Students(student_id=1,name='Oxana', email='oxana@gmail.com',country='UK',native_language='russian',telephone='88766564')
# d.session.add(c1)
# c2 = Students(student_id=2,name='Mark',email='mark@gmail.com',country='Italy',native_language='spanish',telephone='00866564')
# d.session.add(c2)
# c3 = Students(student_id=3,name='Olga',email='olga@gmail.com',country='Germany',native_language='english',telephone='8567564')
# d.session.add(c3)
# c4 = Students(student_id=4,name='Donald',email='donald@gmail.com',country='UK',native_language='english',telephone='88766564')
# d.session.add(c4)
#
# d.session.commit()
#
# p1 = Foreign_language(language_id=1,language_name='Japanese',student_id=1)
# d.session.add(p1)
# p2 = Foreign_language(language_id=2,language_name='Mexican',student_id=1)
# d.session.add(p2)
# p3 = Foreign_language(language_id=3,language_name='Chinese',student_id=3)
# d.session.add(p3)
# p5 = Foreign_language(language_id=4,language_name='Korean',student_id=4)
# d.session.add(p5)
#
# d.session.commit()

# Task - 3 (multiple times)

for std in Students.query.all():
    print("- ",std.name)
    for language in std.foreign_language:
        print("\t - ",language.language_name)
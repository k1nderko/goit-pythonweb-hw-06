from database import SessionLocal
from faker import Faker
import random
from models import Student, Group, Teacher, Subject, Grade, Base

faker = Faker()

db = SessionLocal()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
db.add_all(groups)
db.commit()

teachers = [Teacher(name=faker.name()) for _ in range(5)]
db.add_all(teachers)
db.commit()

subjects = [Subject(name=faker.word(), teacher=random.choice(teachers)) for _ in range(7)]
db.add_all(subjects)
db.commit()

students = [Student(name=faker.name(), group=random.choice(groups)) for _ in range(50)]
db.add_all(students)
db.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 20)):
            grade = Grade(student=student, subject=subject, grade=random.randint(60, 100))
            db.add(grade)

db.commit()

print("Done!")

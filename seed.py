from database import SessionLocal
from faker import Faker
import random
from models import Student, Group, Teacher, Subject, Grade, Base

faker = Faker()

db = SessionLocal()

groups_exist = db.query(Group).count() > 0
teachers_exist = db.query(Teacher).count() > 0
subjects_exist = db.query(Subject).count() > 0
students_exist = db.query(Student).count() > 0

if groups_exist or teachers_exist or subjects_exist or students_exist:
    user_choice = input("База не порожня. Хочете додати нові дані (A) чи переписати існуючі (R)? (A/R): ").strip().lower()
    if user_choice == "r":
        db.query(Group).delete()
        db.query(Teacher).delete()
        db.query(Subject).delete()
        db.query(Student).delete()
        db.query(Grade).delete()
        db.commit()
        print("Існуючі дані переписано.")
    elif user_choice != "a":
        print("Невірний вибір. Завершення роботи.")
        exit()
else:
    print("База порожня. Додаємо нові дані.")

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

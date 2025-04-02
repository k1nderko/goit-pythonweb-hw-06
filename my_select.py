from sqlalchemy import func
from models import Student, Grade, Subject, Group, Teacher
from database import SessionLocal

def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    db = SessionLocal()
    try:
        result = db.query(
            Student.name,
            func.avg(Grade.grade).label('average_grade')
        ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
        return result
    finally:
        db.close()


def select_2(subject_name):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    db = SessionLocal()
    try:
        result = db.query(
            Student.name,
            func.avg(Grade.grade).label('average_grade')
        ).join(Grade).join(Subject).filter(Subject.name == subject_name)\
            .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
        return result
    finally:
        db.close()


def select_3(subject_name):
    """Знайти середній бал у групах з певного предмета."""
    db = SessionLocal()
    try:
        result = db.query(
            Group.name,
            func.avg(Grade.grade).label('average_grade')
        ).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name)\
            .group_by(Group.id).all()
        return result
    finally:
        db.close()


def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    db = SessionLocal()
    try:
        result = db.query(func.avg(Grade.grade).label('average_grade')).scalar()
        return result
    finally:
        db.close()


def select_5(teacher_name):
    """Знайти які курси читає певний викладач."""
    db = SessionLocal()
    try:
        result = db.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
        return result
    finally:
        db.close()


def select_6(group_name):
    """Знайти список студентів у певній групі."""
    db = SessionLocal()
    try:
        result = db.query(Student.name).join(Group).filter(Group.name == group_name).all()
        return result
    finally:
        db.close()


def select_7(group_name, subject_name):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    db = SessionLocal()
    try:
        result = db.query(Student.name, Grade.grade).join(Group).join(Grade).join(Subject)\
            .filter(Group.name == group_name, Subject.name == subject_name).all()
        return result
    finally:
        db.close()


def select_8(teacher_name):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    db = SessionLocal()
    try:
        result = db.query(func.avg(Grade.grade).label('average_grade')).join(Teacher).join(Subject)\
            .filter(Teacher.name == teacher_name).scalar()
        return result
    finally:
        db.close()


def select_9(student_name):
    """Знайти список курсів, які відвідує певний студент."""
    db = SessionLocal()
    try:
        result = db.query(Subject.name).join(Grade).join(Student).filter(Student.name == student_name).all()
        return result
    finally:
        db.close()


def select_10(student_name, teacher_name):
    """Список курсів, які певному студенту читає певний викладач."""
    db = SessionLocal()
    try:
        result = db.query(Subject.name).join(Grade).join(Student).join(Teacher, Teacher.id == Subject.teacher_id) \
            .filter(Student.name == student_name, Teacher.name == teacher_name).all()
        return result
    finally:
        db.close()


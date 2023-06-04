from src.db import session
from src.models import Teacher, Discipline, Group, Student, Grade
from datetime import datetime, timedelta, date
from faker import Faker
from random import randint, choice

disciplines = [
    'Math',
    'Biology',
    'Chemistry',
    'History',
    'Literature',
    'English',
    'Drawing'
]

groups = ['01wj', '9F1', 'W010F']
NUMBER_TEACHER = 5
NUMBER_STUDENTS = 45
fake = Faker()


def create_teachers():
    for _ in range(NUMBER_TEACHER):
        teacher = Teacher(first_name=fake.first_name(), last_name=fake.last_name())
        session.add(teacher)
    session.commit()


def create_discipline():
    t = session.query(Teacher).all()
    for discipline_name in disciplines:
        teacher = choice(t)
        new_discipline = Discipline(name=discipline_name, teacher_id=teacher.id)
        session.add(new_discipline)
    session.commit()


def create_groups():
    for el in groups:
        new_group = Group(name=el)
        session.add(new_group)
    session.commit()


def create_students():
    g = session.query(Group).all()
    for _ in range(NUMBER_STUDENTS):
        group = choice(g)
        student = Student(fullname=fake.name(), group_id=group.id)
        session.add(student)
    session.commit()


def create_grades():
    start_study = datetime.strptime('2022-09-01', '%Y-%m-%d')
    end_study = datetime.strptime('2023-06-15', '%Y-%m-%d')

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        current = start
        while current <= end:
            if current.isoweekday() < 5:
                result.append(current)
            current += timedelta(1)
        return result

    list_dates = get_list_date(start_study, end_study)
    d = session.query(Discipline).all()
    s = session.query(Student).all()
    for day in list_dates:
        random_discipline = choice(d)
        random_students = choice(s)
        grade = Grade(
            discipline_id=random_discipline.id,
            student_id=random_students.id,
            grade=randint(1, 12),
            date_of=day.date()
        )
        session.add(grade)
    session.commit()


if __name__ == '__main__':
    # session.query(Grade).delete()
    # session.query(Student).delete()
    # session.query(Discipline).delete()
    # session.query(Group).delete()
    # session.query(Teacher).delete()
    # session.commit()

    create_teachers()
    create_discipline()
    create_groups()
    create_students()
    create_grades()



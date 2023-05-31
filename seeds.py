from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta, date


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

engine = create_engine('postgresql://postgres:1836@localhost/postgres')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)


class Disciplines(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(ForeignKey('teachers.id'))


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    group_id = Column(ForeignKey('groups.id'))


class Grades(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    discipline_id = Column(ForeignKey('disciplines.id'))
    student_id = Column(ForeignKey('students.id'))
    grade = Column(Integer)
    date_of = Column(Date)


def get_list_date(start: date, end: date) -> list[date]:
    result = []
    current = start
    while current <= end:
        if current.isoweekday() < 5:
            result.append(current)
        current += timedelta(1)
    return result


Base.metadata.create_all(engine)

if __name__ == '__main__':
    start_study = datetime.strptime('2022-09-01', '%Y-%m-%d')
    end_study = datetime.strptime('2023-06-15', '%Y-%m-%d')
    list_dates = get_list_date(start_study, end_study)
    teachers = [fake.name() for _ in range(NUMBER_TEACHER)]
    for el in teachers:
        new_teacher = Teacher(fullname=el)
        session.add(new_teacher)
    t = session.query(Teacher).all()
    for discipline_name in disciplines:
        teacher = choice(t)
        new_discipline = Disciplines(name=discipline_name, teacher_id=teacher.id)
        session.add(new_discipline)
    for el in groups:
        new_group = Group(name=el)
        session.add(new_group)
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    g = session.query(Group).all()
    d = session.query(Disciplines).all()
    for el in students:
        group = choice(g)
        new_student = Student(fullname=el, group_id=group.id)
        session.add(new_student)
        for discipline in d:
            new_grade = Grades(
                discipline_id=discipline.id,
                student_id=new_student.id,
                grade=randint(1, 12),
                date_of=date.today()
            )
            session.add(new_grade)
    session.commit()

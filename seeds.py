from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import psycopg2
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


Base.metadata.create_all(engine)

if __name__ == '__main__':
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
    for el in students:
        group = choice(g)
        new_student = Student(fullname=el, group_id=group.id)
        session.add(new_student)
    session.commit()


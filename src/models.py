from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import relationship

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    discipline = relationship('Discipline', back_populates='teacher')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='discipline')
    grades = relationship('Grade', back_populates='disciplines')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship('Student', back_populates='group')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    group_id = Column(ForeignKey('groups.id'))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    discipline_id = Column(ForeignKey('disciplines.id'))
    student_id = Column(ForeignKey('students.id'))
    grade = Column(Integer)
    date_of = Column(Date)

    student = relationship('Student', back_populates='grades')
    disciplines = relationship('Discipline', back_populates='grades')



from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


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
    date_of = Column(DateTime)

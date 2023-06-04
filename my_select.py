from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session
from pprint import pprint


def select_1():
    result = session.query(Student.fullname,
                           func.round(func.avg(Grade.grade), 2)
                           .label('avg_grade'))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(5)\
        .all()
    return result


def select_2(sub):
    result = session.query(Student.fullname,
                           func.round(func.avg(Grade.grade), 2)
                           .label('avg_grade'))\
        .join(Grade)\
        .join(Discipline)\
        .filter(Discipline.name == sub)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(1)\
        .all()
    return result


def select_3(sub):
    result = session.query(Group.name,
                           func.avg(Grade.grade)
                           .label('avg_grade'))\
        .select_from(Grade)\
        .join(Student)\
        .join(Discipline)\
        .filter(Discipline.name == sub)\
        .filter(Student.group_id == Group.id)\
        .group_by(Group.id)\
        .all()
    return result


def select_4():
    result = session.query(func.round(Grade.grade))\
        .select_from(Grade)\
        .limit(1)\
        .all()
    return result


def select_5():
    result = session.query(Discipline.name,
                           Teacher.first_name,
                           Teacher.last_name)\
        .select_from(Discipline)\
        .join(Teacher)\
        .all()
    return result


def select_6(sub):
    result = session.query(Group.name,
                           Student.fullname)\
        .select_from(Student)\
        .join(Group)\
        .filter(Group.name == sub)\
        .order_by(Group.name)\
        .all()
    return result


def select_7(g, d):
    result = session.query(Student.fullname,
                           Grade.grade,
                           Group.name,
                           Discipline.name)\
        .select_from(Grade)\
        .join(Student)\
        .join(Discipline)\
        .join(Group)\
        .filter(and_(Group.name == g, Discipline.name == d))\
        .order_by(Grade.grade.desc())\
        .all()
    return result


def select_8(teacher_id):
    result = session.query(Teacher.first_name,
                           Teacher.last_name,
                           Discipline.name,
                           func.round(func.avg(Grade.grade)))\
        .select_from(Grade)\
        .join(Discipline)\
        .join(Teacher)\
        .filter(Teacher.id == teacher_id)\
        .group_by(Teacher.first_name, Teacher.last_name, Discipline.name)\
        .all()
    return result


def select_9(student_id):
    result = session.query(Student.fullname,
                           Discipline.name)\
        .select_from(Grade)\
        .join(Discipline)\
        .join(Student)\
        .filter(Student.id == student_id) \
        .group_by(Student.fullname, Discipline.name) \
        .all()
    return result


def select_10(student_id, teacher_id):
    result = session.query(Discipline.name,
                           Student.fullname,
                           Teacher.first_name,
                           Teacher.last_name)\
        .select_from(Grade)\
        .join(Student)\
        .join(Discipline)\
        .join(Teacher)\
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))\
        .all()
    return result




if __name__ == '__main__':
    # List of Disciplines
    # 'Math',
    # 'Biology',
    # 'Chemistry',
    # 'History',
    # 'Literature',
    # 'English',
    # 'Drawing'

    # List of Groups
    # ['01wj', '9F1', 'W010F']

    print('*' * 100)
    pprint(select_1())
    print('*' * 100)
    pprint(select_2('Drawing'))
    print('*' * 100)
    pprint(select_3('Math'))
    print('*' * 100)
    print(select_4())
    print('*' * 100)
    pprint(select_5())
    print('*' * 100)
    pprint(select_6('9F1'))
    print('*' * 100)
    pprint(select_7('01wj', 'Biology'))
    print('*' * 100)
    pprint(select_8(2))
    print('*' * 100)
    pprint(select_9(34))
    print('*' * 100)
    pprint(select_10(44, 2))
    print('*' * 100)




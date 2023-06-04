from db import session
from models import Teacher, Discipline, Group, Student, Grade
from datetime import datetime
from random import randint, choice
import argparse


parser = argparse.ArgumentParser(description='crud')
parser.add_argument('-a', '--action', choices=['create', 'read', 'update', 'delete'])
parser.add_argument('-m', '--model', choices=['Teacher', 'Discipline', 'Group', 'Student', 'Grade'])
parser.add_argument('--name')
parser.add_argument('--id', type=int)
args = vars(parser.parse_args())
action = args.get('action')
model = args.get('model')
name = args.get('name')
id = args.get('id')


def create(model, name):
    if model == 'Teacher':
        teacher = Teacher(first_name=name.split()[0], last_name=name.split()[1])
        session.add(teacher)
        session.commit()
        return f'Created successfully {model}'
    elif model == 'Discipline':
        t = session.query(Teacher).all()
        random_teacher = choice(t)
        discipline = Discipline(name=name, teacher_id=random_teacher.id)
        session.add(discipline)
        session.commit()
        return f'Created successfully {model}'
    elif model == 'Group':
        group = Group(name=name)
        session.add(group)
        session.commit()
        return f'Created successfully {model}'
    elif model == 'Student':
        g = session.query(Group).all()
        random_group = choice(g)
        student = Student(fullname=name, group_id=random_group.id)
        session.add(student)
        session.commit()
        return f'Created successfully {model}'
    elif model == 'Grade':
        d = session.query(Discipline).all()
        random_discipline = choice(d)
        s = session.query(Student).all()
        random_student = session.query(Student).all()
        grade =  Grade(discipline_id=random_discipline.id, student_id=random_student.id, grade=randint(1,12), date_of=datetime.today())
        session.add(grade)
        session.commit()
        return f'Created successfully {model}'


def read(model, id=None):
    if model == 'Teacher':
        if id:
            teacher = session.get(Teacher, id)
            if teacher:
                return f"Teacher ID: {teacher.id}, Name: {teacher.first_name} {teacher.last_name}"
            else:
                return 'Teacher not found'
        else:
            teachers = session.query(Teacher).all()
            return [teacher + '\n' for teacher in teachers]
    elif model == 'Discipline':
        if id:
            discipline = session.get(Discipline, id)
            if discipline:
                return f"Discipline ID: {discipline.id}, Name: {discipline.name}"
            else:
                return 'Discipline not found'
        else:
            disciplines = session.query(Discipline).all()
            return [discipline + '\n' for discipline in disciplines]
    elif model == 'Group':
        if id:
            group = session.get(Group, id)
            if group:
                return f"Group ID: {group.id}, Name: {group.name}"
            else:
                return 'Group not found'
        else:
            groups = session.query(Group).all()
            return [group + '\n' for group in groups]
    elif model == 'Student':
        if id:
            student = session.get(Student, id)
            if student:
                return f"Student ID: {student.id}, Name: {student.fullname}"
            else:
                return 'Student not found'
        else:
            students = session.query(Student).all()
            return [student + '\n' for student in students]
    elif model == 'Grade':
        if id:
            student = session.get(Grade, id)
            if student:
                return f"Grade ID: {student.id}, Discipline: {Grade.discipline_id}, Student: {Grade.student_id}, Grade: {Grade.grade}, Date: {Grade.date_of}"
            else:
                return 'Grade not found'
        else:
            grades = session.query(Grade).all()
            return [grade + '\n' for grade in grades]


def update(model, id, name):
    if model == 'Teacher':
        teacher = session.get(Teacher, id)
        if teacher:
            teacher.first_name = name.split()[0]
            teacher.last_name = name.split()[1]
            session.commit()
            return f'Updated successfully {model}'
        else:
            return 'Teacher not found'
    elif model == 'Discipline':
        discipline = session.get(Discipline, id)
        if discipline:
            discipline.name = name
            session.commit()
            return f'Updated successfully {model}'
        else:
            return 'Discipline not found'
    elif model == 'Group':
        group = session.get(Group, id)
        if group:
            group.name = name
            session.commit()
            return f'Updated successfully {model}'
        else:
            return 'Group not found'
    elif model == 'Student':
        student = session.get(Student, id)
        if student:
            student.fullname = name
            session.commit()
            return f'Updated successfully {model}'
        else:
            return 'Student not found'


def delete(model, id):
    if model == 'Teacher':
        teacher = session.get(Teacher, id)
        if teacher:
            session.delete(teacher)
            session.commit()
            return f'Deleted successfully {model}'
        else:
            return 'Teacher not found'
    elif model == 'Discipline':
        discipline = session.get(Discipline, id)
        if discipline:
            session.delete(discipline)
            session.commit()
            return f'Deleted successfully {model}'
        else:
            return 'Discipline not found'
    elif model == 'Group':
        group = session.get(Group, id)
        if group:
            session.delete(group)
            session.commit()
            return f'Deleted successfully {model}'
        else:
            return 'Group not found'
    elif model == 'Student':
        student = session.get(Student, id)
        if student:
            session.delete(student)
            session.commit()
            return f'Deleted successfully {model}'
        else:
            return 'Student not found'
    elif model == 'Grade':
        grade = session.get(Grade, id)
        if grade:
            session.delete(grade)
            session.commit()
            return f'Deleted successfully {model}'
        else:
            return 'Grade not found'


if __name__ == '__main__':
    if action and model:
        if action == "create":
            res = create(model, name)
            print(res)
        elif action == "read":
            res = read(model, id)
            print(res)
        elif action == "update":
            res = update(model, id, name)
            print(res)
        elif action == "delete":
            res = delete(model, id)
            print(res)
    else:
        print("Please provide both --action and --model arguments.")

from app.models import Group, Course
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import csv
import datetime

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
session = Session()

courses_data = csv.DictReader(open('import_data/courses.csv'))
groups_data = csv.DictReader(open('import_data/groups.csv'))

for course_item in courses_data:
    session.add(Course(title=course_item.get('title')))

session.commit()

for group_item in groups_data:
    date = datetime.datetime.strptime(group_item.get('start_at'), '%d.%m.%Y')
    course = session.query(Course).filter(Course.title == group_item.get('course')).first()

    group = Group(id=group_item.get('id'), title=group_item.get('title'), status=group_item.get('status'),
                  course=course, seats=group_item.get('seats'), start_at=date.date())

    session.add(group)

session.commit()

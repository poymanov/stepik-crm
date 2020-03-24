from app.models import Group
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import csv
import datetime

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
session = Session()

groups_data = csv.DictReader(open('import_data/groups.csv'))

for group_item in groups_data:
    date = datetime.datetime.strptime(group_item.get('start_at'), '%d.%m.%Y')
    group = Group(id=group_item.get('id'), title=group_item.get('title'), status=group_item.get('status'),
                  course=group_item.get('course'), seats=group_item.get('seats'), start_at=date.date())

    session.add(group)

session.commit()

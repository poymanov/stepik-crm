from flask import Flask, session

from app.config import Config
from app.models import db, Group, GroupStatus, Course
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babelex import Babel
from app.admin import GroupModelView, CourseModelView
from app.admin import CourseModelView

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app, name='Stepik CRM')

db.init_app(app)
migrate = Migrate(app, db)

babel = Babel(app)


@babel.localeselector
def get_locale():
    return session.get('lang', 'ru')


from app.views import *

admin.add_view(CourseModelView(Course, db.session, name='Курсы'))
admin.add_view(GroupModelView(Group, db.session, name='Группы'))

from flask import Flask, session

from app.config import Config
from app.models import db, Group, GroupStatus, Course, Applicant, ApplicantStatus
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babelex import Babel
from app.admin import GroupModelView, CourseModelView, ApplicantModelView, DashboardView
from app.admin import CourseModelView

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app, name='Stepik CRM', index_view=DashboardView())

db.init_app(app)
migrate = Migrate(app, db)

babel = Babel(app)


@babel.localeselector
def get_locale():
    return session.get('lang', 'ru')


from app.views import *

admin.add_view(CourseModelView(Course, db.session, name='Курсы'))
admin.add_view(GroupModelView(Group, db.session, name='Группы'))
admin.add_view(ApplicantModelView(Applicant, db.session, name='Заявки'))

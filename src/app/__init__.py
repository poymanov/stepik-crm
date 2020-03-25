from flask import Flask, session, url_for
from app.config import Config
from app.models import db, Group, GroupStatus, Course, Applicant, ApplicantStatus, User
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babelex import Babel
from app.admin import GroupModelView, CourseModelView, ApplicantModelView, DashboardView, MailerView, UserModelView
from app.admin import CourseModelView
from app.mailer import mail
from flask_admin.menu import MenuLink

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app, name='Stepik CRM', template_mode='bootstrap3', index_view=DashboardView())

db.init_app(app)
migrate = Migrate(app, db)

babel = Babel(app)

mail.init_app(app)


@babel.localeselector
def get_locale():
    return session.get('lang', 'ru')


from app.views import *

admin.add_view(CourseModelView(Course, db.session, name='Курсы'))
admin.add_view(GroupModelView(Group, db.session, name='Группы'))
admin.add_view(ApplicantModelView(Applicant, db.session, name='Заявки'))
admin.add_view(MailerView(name='Рассылки', endpoint='mailer'))
admin.add_view(UserModelView(User, db.session, name='Пользователи'))
admin.add_link(MenuLink(name='Выход', url='/logout'))

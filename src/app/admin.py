from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView
from app.models import db, GroupStatus, ApplicantStatus, Applicant, Group
from flask_admin import AdminIndexView, expose, BaseView
from app.forms import MailerForm
from app.mailer import send_to_user
import app.services.users as users_service


def is_accessible():
    return users_service.get_auth_user() is not None


def inaccessible_callback_url():
    return url_for('login', next=request.url)


class GroupModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('title', 'status', 'course', 'start_at', 'applicants', 'seats')

    column_labels = dict(title='Название', status='Статус', course='Курс', start_at='Старт', applicants='Набрано',
                         seats='Макс. человек')

    column_formatters = dict(status=lambda v, c, m, p: GroupStatus(m.status).value,
                             start_at=lambda v, c, m, p: m.start_at.strftime('%d.%m.%Y'),
                             applicants=lambda v, c, m, p: len(m.applicants))

    form_excluded_columns = 'applicants'

    def is_accessible(self):
        return is_accessible()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(inaccessible_callback_url())


class CourseModelView(ModelView):
    list_template = 'admin/list.html'

    column_labels = dict(title='Название')

    form_excluded_columns = ('groups', 'applicants')

    def is_accessible(self):
        return is_accessible()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(inaccessible_callback_url())


class ApplicantModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('name', 'phone', 'email', 'course', 'status', 'group')

    column_labels = dict(name='Имя', phone='Телефон', email='Email', course='Курс', status='Статус', group='Группа')

    column_formatters = dict(status=lambda v, c, m, p: ApplicantStatus(m.status).value)

    def is_accessible(self):
        return is_accessible()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(inaccessible_callback_url())


class DashboardView(AdminIndexView):
    @expose('/')
    def index(self):
        applicants = {
            'assigned': db.session.query(Applicant).filter(Applicant.group != None).count(),
            'not_assigned': db.session.query(Applicant).filter(Applicant.group == None).count(),
            'last': db.session.query(Applicant).filter(Applicant.group == None,
                                                       Applicant.status == ApplicantStatus.NEW).order_by(
                Applicant.id.desc()).limit(3).all()
        }

        groups = db.session.query(Group).order_by(Group.start_at.asc()).limit(3).all()

        return self.render('admin/index.html', applicants=applicants, groups=groups)

    def is_accessible(self):
        return is_accessible()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(inaccessible_callback_url())


class MailerView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        form = MailerForm()
        if form.validate_on_submit():
            send_to_user(form.email.data, form.subject.data,
                         self.render('admin/mailer/mail-template.html', text=form.text.data))
            return self.render('admin/mailer/sent.html', form=form)
        else:
            return self.render('admin/mailer/new.html', form=form)

    def is_accessible(self):
        return is_accessible()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(inaccessible_callback_url())


class UserModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('name', 'email')

    column_labels = dict(name='Имя', email='Email')

    form_excluded_columns = 'password'

    can_create = False

    def is_accessible(self):
        return is_accessible()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(inaccessible_callback_url())

from flask_admin.contrib.sqla import ModelView
from app.models import db, GroupStatus, ApplicantStatus, Applicant, Group
from flask_admin import AdminIndexView, expose, BaseView
from app.forms import MailerForm
from app.mailer import mail, send_to_user


class GroupModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('title', 'status', 'course', 'start_at', 'applicants', 'seats')

    column_labels = dict(title='Название', status='Статус', course='Курс', start_at='Старт', applicants='Набрано',
                         seats='Макс. человек')

    column_formatters = dict(status=lambda v, c, m, p: GroupStatus(m.status).value,
                             start_at=lambda v, c, m, p: m.start_at.strftime('%d.%m.%Y'),
                             applicants=lambda v, c, m, p: len(m.applicants))

    form_excluded_columns = 'applicants'


class CourseModelView(ModelView):
    list_template = 'admin/list.html'

    column_labels = dict(title='Название')

    form_excluded_columns = ('groups', 'applicants')


class ApplicantModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('name', 'phone', 'email', 'course', 'status', 'group')

    column_labels = dict(name='Имя', phone='Телефон', email='Email', course='Курс', status='Статус', group='Группа')

    column_formatters = dict(status=lambda v, c, m, p: ApplicantStatus(m.status).value)


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


class MailerView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        form = MailerForm()
        if form.validate_on_submit():
            send_to_user(form.data.get('email'), form.data.get('subject'),
                         self.render('admin/mailer/mail-template.html', text=form.data.get('text')))
            return self.render('admin/mailer/sent.html', form=form)
        else:
            return self.render('admin/mailer/new.html', form=form)

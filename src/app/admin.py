from flask_admin.contrib.sqla import ModelView
from app.models import GroupStatus, ApplicantStatus


class GroupModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('title', 'status', 'course', 'start_at', 'applicants', 'seats')

    column_labels = dict(title='Название', status='Статус', course='Курс', start_at='Старт', applicants='Набрано', seats='Макс. человек')

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

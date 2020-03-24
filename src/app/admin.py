from flask_admin.contrib.sqla import ModelView
from app.models import GroupStatus, Group


class GroupModelView(ModelView):
    list_template = 'admin/list.html'

    column_list = ('title', 'status', 'course', 'start_at', 'seats')

    column_labels = dict(title='Название', status='Статус', course='Предмет', start_at='Старт', seats='Макс. человек')

    column_formatters = dict(status=lambda v, c, m, p: GroupStatus(m.status).value,
                             start_at=lambda v, c, m, p: m.start_at.strftime('%d.%m.%Y'),
                             course=lambda v, c, m, p: m.course.title)


class CourseModelView(ModelView):
    list_template = 'admin/list.html'

    column_labels = dict(title='Название')

    form_excluded_columns = 'groups'

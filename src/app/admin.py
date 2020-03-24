from flask_admin.contrib.sqla import ModelView
from app.models import GroupStatus


class GroupModelView(ModelView):
    list_template = 'admin/group/list.html'

    column_list = ('title', 'status', 'course', 'start_at', 'seats')

    column_labels = dict(title='Название', status='Статус', course='Предмет', start_at='Старт', seats='Макс. человек')

    column_formatters = dict(status=lambda v, c, m, p: GroupStatus(m.status).value,
                             start_at=lambda v, c, m, p: m.start_at.strftime('%d.%m.%Y'))

    form_choices = {
        'status': [
            (GroupStatus.RECRUITS, GroupStatus.RECRUITS.value),
            (GroupStatus.RECRUITED, GroupStatus.RECRUITED.value),
            (GroupStatus.IN_PROGRESS, GroupStatus.IN_PROGRESS.value),
            (GroupStatus.ARCHIVED, GroupStatus.ARCHIVED.value)
        ]
    }

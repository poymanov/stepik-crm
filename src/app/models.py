from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

    groups = db.relationship('Group', back_populates='course')

    def __str__(self):
        return self.title


class GroupStatus(enum.Enum):
    RECRUITS = 'Набирается'
    RECRUITED = 'Набрана'
    IN_PROGRESS = 'Идёт'
    ARCHIVED = 'В архиве'


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(GroupStatus), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    start_at = db.Column(db.Date, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    course = db.relationship('Course', back_populates='groups')

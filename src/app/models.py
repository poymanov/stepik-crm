from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


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
    course = db.Column(db.String(255), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    start_at = db.Column(db.Date, nullable=False)

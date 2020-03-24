"""002 groups

Revision ID: a7fca0ffa15d
Revises: 0339807ce820
Create Date: 2020-03-24 18:30:00.883739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7fca0ffa15d'
down_revision = '0339807ce820'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Enum('RECRUITS', 'RECRUITED', 'IN_PROGRESS', 'ARCHIVED', name='groupstatus'), nullable=False),
    sa.Column('seats', sa.Integer(), nullable=False),
    sa.Column('start_at', sa.Date(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups')
    # ### end Alembic commands ###
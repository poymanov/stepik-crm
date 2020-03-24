"""003 applicants

Revision ID: 2e404f613f08
Revises: a7fca0ffa15d
Create Date: 2020-03-24 19:31:01.641658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e404f613f08'
down_revision = 'a7fca0ffa15d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applicants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Enum('NEW', 'PROCESS', 'PAYED', 'ASSIGNED_TO_GROUP', name='applicantstatus'), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applicants')
    # ### end Alembic commands ###
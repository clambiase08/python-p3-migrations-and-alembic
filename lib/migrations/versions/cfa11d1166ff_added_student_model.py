"""Added Student model

Revision ID: cfa11d1166ff
Revises: 79abf39b839f
Create Date: 2023-08-01 10:26:21.198611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfa11d1166ff'
down_revision = '79abf39b839f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=55), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('enrolled_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_name'), 'students', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_name'), table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###

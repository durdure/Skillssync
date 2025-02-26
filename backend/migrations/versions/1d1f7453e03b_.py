"""empty message

Revision ID: 1d1f7453e03b
Revises: 1cc99debf476
Create Date: 2024-02-15 22:18:44.575415

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1d1f7453e03b'
down_revision = '1cc99debf476'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mentor_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['mentor_id'], ['mentor.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('session')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mentor_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', mysql.DATETIME(), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=20), nullable=True),
    sa.ForeignKeyConstraint(['mentor_id'], ['mentor.id'], name='session_ibfk_3'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='session_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('request')
    # ### end Alembic commands ###

"""empty message

Revision ID: a6d42cf0426b
Revises: af385e089a63
Create Date: 2024-02-15 00:53:36.364498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6d42cf0426b'
down_revision = 'af385e089a63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_file', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('bio', sa.String(length=1000), nullable=True),
    sa.Column('phone_no', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('mentor', sa.Boolean(), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.Column('confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('mentor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('profession', sa.String(length=100), nullable=True),
    sa.Column('job_title', sa.String(length=100), nullable=True),
    sa.Column('company', sa.String(length=100), nullable=True),
    sa.Column('skills', sa.String(length=200), nullable=True),
    sa.Column('availability', sa.String(length=200), nullable=True),
    sa.Column('languages_spoken', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('mentor')
    op.drop_table('user')
    # ### end Alembic commands ###

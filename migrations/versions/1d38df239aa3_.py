"""empty message

Revision ID: 1d38df239aa3
Revises: 2993fb38fea5
Create Date: 2019-07-01 23:59:08.751984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d38df239aa3'
down_revision = '2993fb38fea5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('aboutme', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'aboutme')
    # ### end Alembic commands ###

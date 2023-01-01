"""empty message

Revision ID: ccbfb61eda0d
Revises: 11ba83e2dd71
Create Date: 2021-11-17 11:52:12.160638

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccbfb61eda0d'
down_revision = '11ba83e2dd71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coupon', sa.Column('comment', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('coupon', 'comment')
    # ### end Alembic commands ###

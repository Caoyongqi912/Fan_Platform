"""empty message

Revision ID: 05f52e4eda1c
Revises: 6a4d5e3a9a27
Create Date: 2020-07-16 16:40:07.893183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05f52e4eda1c'
down_revision = '6a4d5e3a9a27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=12), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###

"""empty message

Revision ID: 4260a7d2ee9d
Revises: aaec7c85043a
Create Date: 2020-08-18 17:49:32.791244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4260a7d2ee9d'
down_revision = 'aaec7c85043a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('steps', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('steps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###

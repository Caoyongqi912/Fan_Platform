"""empty message

Revision ID: aaec7c85043a
Revises: 0ce0485d249a
Create Date: 2020-08-18 17:27:54.549510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaec7c85043a'
down_revision = '0ce0485d249a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('steps', schema=None) as batch_op:
        batch_op.drop_column('t')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('steps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('t', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###

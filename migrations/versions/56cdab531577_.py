"""empty message

Revision ID: 56cdab531577
Revises: 96e120770bbb
Create Date: 2023-11-10 22:24:33.183252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56cdab531577'
down_revision = '96e120770bbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###

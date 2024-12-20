"""adding secret for auth to user

Revision ID: 41a48a81ec4c
Revises: 
Create Date: 2024-12-20 11:43:59.231063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41a48a81ec4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('secret', sa.String(length=32), nullable=True))
        batch_op.create_unique_constraint('uq_user_secret', ['secret'])
    

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint('uq_user_secret', type_='unique')
        batch_op.drop_column('secret')

    # ### end Alembic commands ###
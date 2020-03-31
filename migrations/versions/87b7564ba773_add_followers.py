"""add followers

Revision ID: 87b7564ba773
Revises: 34ef547b28f9
Create Date: 2020-03-31 09:39:24.802156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87b7564ba773'
down_revision = '34ef547b28f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

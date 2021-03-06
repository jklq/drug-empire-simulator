"""empty message

Revision ID: c30bb15af935
Revises: cc761b06d759
Create Date: 2021-03-22 18:49:40.861302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c30bb15af935'
down_revision = 'cc761b06d759'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(length=1), nullable=True),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mafia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(length=1), nullable=True),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mafia')
    op.drop_table('cartel')
    # ### end Alembic commands ###

"""empty message

Revision ID: cc761b06d759
Revises: c66e49fd37f9
Create Date: 2021-03-22 17:02:15.172135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc761b06d759'
down_revision = 'c66e49fd37f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('broker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(length=1), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user')
    )
    op.create_table('vessel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('fuel_efficiency', sa.Integer(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('detection_rate', sa.Integer(), nullable=True),
    sa.Column('trips', sa.Integer(), nullable=True),
    sa.Column('mileage', sa.Integer(), nullable=True),
    sa.Column('profits', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['broker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vessel')
    op.drop_table('broker')
    # ### end Alembic commands ###
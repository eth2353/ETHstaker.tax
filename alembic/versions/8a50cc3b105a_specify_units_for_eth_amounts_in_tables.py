"""Specify units for Eth amounts in tables

Revision ID: 8a50cc3b105a
Revises: e2344e393641
Create Date: 2023-04-27 09:57:42.839662

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8a50cc3b105a'
down_revision = 'e2344e393641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('withdrawal', 'amount', new_column_name='amount_gwei', type_=sa.Numeric(precision=18, scale=0))
    op.alter_column('block_reward', 'priority_fees', new_column_name='priority_fees_wei')
    op.alter_column('block_reward', 'mev_reward_value', new_column_name='mev_reward_value_wei')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('block_reward', 'mev_reward_value_wei',
                    new_column_name='mev_reward_value')
    op.alter_column('block_reward', 'priority_fees_wei',
                    new_column_name='priority_fees')
    op.alter_column('withdrawal', 'amount_gwei', new_column_name='amount', type_=sa.Numeric(precision=27, scale=0))
    # ### end Alembic commands ###

"""add foreign key to onboarding

Revision ID: f0f87d211d96
Revises: 120da5d24dac
Create Date: 2024-10-02 23:44:09.166191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0f87d211d96'
down_revision = '120da5d24dac'
branch_labels = None
depends_on = None


def upgrade():
    # Using batch mode to alter the 'onboardings' table for SQLite compatibility
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_onboardings_employee_id_employees', 'employees', ['employee_id'], ['id'])


def downgrade():
    # Using batch mode for downgrading changes
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')

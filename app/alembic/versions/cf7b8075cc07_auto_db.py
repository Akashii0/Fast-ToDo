"""auto-db

Revision ID: cf7b8075cc07
Revises: 7de1d11a15dc
Create Date: 2024-11-07 18:46:05.370431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf7b8075cc07'
down_revision = '7de1d11a15dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('ToDos_users_fk', source_table="ToDos", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Todos_users_fk', table_name='ToDos')
    pass
    # ### end Alembic commands ###

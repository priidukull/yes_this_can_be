"""Changes to paragraph table: Add default for pg_index_number and a unique index made up of three columns

Revision ID: 2fb8d295822
Revises: 195edb1e86f
Create Date: 2014-09-14 18:45:04.321059

"""

# revision identifiers, used by Alembic.
revision = '2fb8d295822'
down_revision = '195edb1e86f'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.alter_column(table_name="paragraph", column_name="pg_index_number", server_default="0", nullable=False)
    op.create_unique_constraint(source="paragraph", name="pg_uq", local_cols=["statute_id", "pg_number", "pg_index_number"])


def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_constraint(name="pg_uq", table_name="paragraph")
    op.alter_column(table_name="paragraph", column_name="pg_index_number", server_default=None, nullable=True)




def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


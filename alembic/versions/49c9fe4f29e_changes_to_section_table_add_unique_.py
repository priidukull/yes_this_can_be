"""changes to section table: add unique constraint

Revision ID: 49c9fe4f29e
Revises: 2fb8d295822
Create Date: 2014-09-17 08:13:21.002875

"""

# revision identifiers, used by Alembic.
revision = '49c9fe4f29e'
down_revision = '2fb8d295822'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.create_unique_constraint(source="section", name="sc_uq", local_cols=["paragraph_id", "sc_number", "sc_index_number"])

def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_constraint(name="sc_uq", table_name="section")




def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


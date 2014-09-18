"""changes to point table: add unique constraint

Revision ID: 39cfe81ae63
Revises: 49c9fe4f29e
Create Date: 2014-09-17 08:26:14.190734

"""

# revision identifiers, used by Alembic.
revision = '39cfe81ae63'
down_revision = '49c9fe4f29e'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.add_column("point", sa.Column("pt_index_number", sa.Integer, nullable=False, server_default="0"))
    op.create_unique_constraint(source="point", name="pt_uq", local_cols=["section_id", "pt_number", "pt_index_number"])


def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_constraint(name="sc_uq", table_name="section")
    op.drop_column("point", "pt_index_number")





def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


"""create paragraph table

Revision ID: 2177db5d284
Revises: cd1818e5cc
Create Date: 2014-07-12 20:10:59.920844

"""

# revision identifiers, used by Alembic.
revision = '2177db5d284'
down_revision = 'cd1818e5cc'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.create_table(
        "paragraph",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("pg_header", sa.Unicode),
        sa.Column("pg_number", sa.Integer, nullable=False),
        sa.Column("pg_index_number", sa.Integer),
        sa.Column("pg_xml", sa.UnicodeText, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.text("NOW()")),
        sa.Column("statute_id", sa.BigInteger, sa.ForeignKey("statute.id")))



def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_table("paragraph")




def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


"""section table

Revision ID: 57eedd823f7
Revises: 2177db5d284
Create Date: 2014-09-06 13:48:34.684846

"""

# revision identifiers, used by Alembic.
revision = '57eedd823f7'
down_revision = '2177db5d284'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.create_table(
        "section",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("sc_xml", sa.UnicodeText, nullable=False),
        sa.Column("sc_number", sa.Integer, nullable=False),
        sa.Column("sc_index_number", sa.Integer, nullable=False, server_default="0"),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.text("NOW()")),
        sa.Column("paragraph_id", sa.BigInteger, sa.ForeignKey("paragraph.id"), nullable=False))


def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_table("section")



def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


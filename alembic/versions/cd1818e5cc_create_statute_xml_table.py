"""create statute_xml table

Revision ID: cd1818e5cc
Revises: 3695a93b955
Create Date: 2014-07-01 22:25:56.945469

"""

# revision identifiers, used by Alembic.
revision = 'cd1818e5cc'
down_revision = '3695a93b955'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.create_table(
         "statute_xml",
         sa.Column("id", sa.BigInteger, primary_key=True),
         sa.Column("url", sa.Unicode, unique=True, nullable=False),
         sa.Column("xml", sa.UnicodeText, nullable=False),
         sa.Column("updated_at", sa.DateTime, nullable=False, unique=True, server_default=sa.text("NOW()")),
         sa.Column("statute_id", sa.BigInteger, sa.ForeignKey("statute.id")))

def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_table("statute_xml")


def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


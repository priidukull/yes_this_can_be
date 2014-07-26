"""create statutes table

Revision ID: 3695a93b955
Revises: None
Create Date: 2014-07-01 22:16:48.109215

"""

# revision identifiers, used by Alembic.
revision = '3695a93b955'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.create_table(
        "statute",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("name", sa.Unicode, nullable=False, unique=True),
        sa.Column("short_name", sa.Unicode, nullable=False, unique=True))

def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_table("statute")


def upgrade_engine1():
    pass

def downgrade_engine1():
    pass

def upgrade_engine2():
    pass

def downgrade_engine2():
    pass



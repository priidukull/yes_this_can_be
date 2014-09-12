"""create points table

Revision ID: 195edb1e86f
Revises: 57eedd823f7
Create Date: 2014-09-12 08:09:07.592069

"""

# revision identifiers, used by Alembic.
revision = '195edb1e86f'
down_revision = '57eedd823f7'

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    eval("upgrade_%s" % engine_name)()
    op.create_table(
        "point",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("pt_text", sa.UnicodeText, nullable=False),
        sa.Column("pt_number", sa.Integer, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.text("NOW()")),
        sa.Column("section_id", sa.BigInteger, sa.ForeignKey("section.id"), nullable=False))


def downgrade(engine_name):
    eval("downgrade_%s" % engine_name)()
    op.drop_table("point")




def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass


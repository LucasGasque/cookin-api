"""merging two heads

Revision ID: e9b041922066
Revises: c05740a9af49, c021898cde66
Create Date: 2022-03-02 15:40:34.161003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9b041922066'
down_revision = ('c05740a9af49', 'c021898cde66')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass

"""empty message

Revision ID: c38568024f7f
Revises: ccfe7043c280
Create Date: 2022-03-02 15:50:23.640435

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c38568024f7f'
down_revision = 'ccfe7043c280'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_recipes',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('recipe_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.auth_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'recipe_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_recipes')
    # ### end Alembic commands ###

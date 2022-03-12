"""add content column to posts table

Revision ID: 94fd52d38562
Revises: cd0eadd2495c
Create Date: 2022-03-12 12:28:12.944768

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '94fd52d38562'
down_revision = 'cd0eadd2495c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

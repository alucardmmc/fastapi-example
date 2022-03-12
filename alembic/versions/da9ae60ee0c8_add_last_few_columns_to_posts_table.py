"""add last few columns to posts table

Revision ID: da9ae60ee0c8
Revises: 651c1ada6194
Create Date: 2022-03-12 13:15:27.538904

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'da9ae60ee0c8'
down_revision = '651c1ada6194'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False,
                                     server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False,
                                     server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

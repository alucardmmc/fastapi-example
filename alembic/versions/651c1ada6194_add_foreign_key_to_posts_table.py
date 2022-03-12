"""add foreign-key to posts table

Revision ID: 651c1ada6194
Revises: cf04a972e7a0
Create Date: 2022-03-12 13:02:55.871265

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '651c1ada6194'
down_revision = 'cf04a972e7a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table="users", local_cols=['owner_id'],
                          remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column("posts", 'owner_id')
    pass

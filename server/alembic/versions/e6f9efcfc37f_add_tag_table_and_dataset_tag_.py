"""Add Tag table and DataSet-Tag association table

Revision ID: e6f9efcfc37f
Revises: bdab99f87e3e
Create Date: 2019-07-30 14:29:13.062831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f9efcfc37f'
down_revision = 'bdab99f87e3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('data_set_tag_association',
    sa.Column('data_set_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['data_set_id'], ['data_sets.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.UniqueConstraint('data_set_id', 'tag_id', name='uniq_tag_assoc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_set_tag_association')
    op.drop_table('tags')
    # ### end Alembic commands ###

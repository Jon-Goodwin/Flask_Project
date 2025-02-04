"""new fields in user model

Revision ID: 3d444ee0f3a0
Revises: 583a2c13f1e6
Create Date: 2025-01-24 19:48:14.978361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d444ee0f3a0'
down_revision = '583a2c13f1e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=140),
               existing_nullable=False)
        batch_op.drop_index('ix_post_body')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index('ix_post_body', ['body'], unique=1)
        batch_op.alter_column('body',
               existing_type=sa.String(length=140),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###

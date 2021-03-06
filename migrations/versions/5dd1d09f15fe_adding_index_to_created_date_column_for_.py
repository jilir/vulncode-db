"""Adding index to created_date column for the vulnerability table and pubished_date for the nvd_jsons table.

Revision ID: 5dd1d09f15fe
Revises: 32ded3390554
Create Date: 2019-07-03 18:21:52.819263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd1d09f15fe'
down_revision = '32ded3390554'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_vulnerability_date_created'), 'vulnerability', ['date_created'], unique=False)
    op.create_index('idx_nvd_jsons_published_date', 'nvd_jsons', ['published_date'], unique=False, schema='cve')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_nvd_jsons_published_date', table_name='nvd_jsons', schema='cve')
    op.drop_index(op.f('ix_vulnerability_date_created'), table_name='vulnerability')
    # ### end Alembic commands ###

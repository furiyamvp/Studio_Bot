"""empty message

Revision ID: 3d84d3bd4500
Revises: de799edaf282
Create Date: 2024-08-22 12:40:27.801521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d84d3bd4500'
down_revision: Union[str, None] = 'de799edaf282'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.drop_column('users', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###

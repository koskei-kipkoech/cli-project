"""creates students table

Revision ID: 204a6d84ad52
Revises: 26615639e707
Create Date: 2024-12-16 11:34:46.923606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '204a6d84ad52'
down_revision: Union[str, None] = '26615639e707'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

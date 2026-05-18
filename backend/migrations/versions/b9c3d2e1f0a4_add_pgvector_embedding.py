"""add embedding column to training_chunks (JSONB, no pgvector required)

Revision ID: b9c3d2e1f0a4
Revises: a7d4c33dddeb
Create Date: 2026-05-09 01:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b9c3d2e1f0a4'
down_revision: Union[str, Sequence[str], None] = 'a7d4c33dddeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TABLE training_chunks ADD COLUMN IF NOT EXISTS embedding JSONB")


def downgrade() -> None:
    op.drop_column('training_chunks', 'embedding')

"""init2

Revision ID: 993089d41e44
Revises: c57a9ca18c5a
Create Date: 2025-03-26 15:54:14.534265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '993089d41e44'
down_revision: Union[str, None] = 'c57a9ca18c5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_items', sa.Column('order_id', sa.Uuid(), nullable=False))
    op.add_column('order_items', sa.Column('product_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(op.f('fk_order_items_order_id_orders'), 'order_items', 'orders', ['order_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(op.f('fk_order_items_product_id_products'), 'order_items', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('fk_orders_customer_id_customers', 'orders', type_='foreignkey')
    op.create_foreign_key(op.f('fk_orders_customer_id_customers'), 'orders', 'customers', ['customer_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_orders_customer_id_customers'), 'orders', schema='public', type_='foreignkey')
    op.create_foreign_key('fk_orders_customer_id_customers', 'orders', 'customers', ['customer_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(op.f('fk_order_items_product_id_products'), 'order_items', schema='public', type_='foreignkey')
    op.drop_constraint(op.f('fk_order_items_order_id_orders'), 'order_items', schema='public', type_='foreignkey')
    op.drop_column('order_items', 'product_id')
    op.drop_column('order_items', 'order_id')
    # ### end Alembic commands ###

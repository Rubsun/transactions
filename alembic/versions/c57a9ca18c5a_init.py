"""init

Revision ID: c57a9ca18c5a
Revises: 
Create Date: 2025-03-26 15:17:59.683182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c57a9ca18c5a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_customers')),
    schema='public'
    )
    op.create_table('order_items',
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('sub_total', sa.Float(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order_items')),
    schema='public'
    )
    op.create_table('products',
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_products')),
    schema='public'
    )
    op.create_table('orders',
    sa.Column('customer_id', sa.Uuid(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['public.customers.id'], name=op.f('fk_orders_customer_id_customers'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orders')),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders', schema='public')
    op.drop_table('products', schema='public')
    op.drop_table('order_items', schema='public')
    op.drop_table('customers', schema='public')
    # ### end Alembic commands ###

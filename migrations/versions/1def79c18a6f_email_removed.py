"""email removed

Revision ID: 1def79c18a6f
Revises: 7dba049c37ca
Create Date: 2023-03-02 11:53:32.015379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1def79c18a6f'
down_revision = '7dba049c37ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('t_additoinalfield_ibfk_1', 'T_additoinalfield', type_='foreignkey')
    op.create_foreign_key(None, 'T_additoinalfield', 'T_lead', ['additoinalfield_lead_id'], ['lead_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_affiliate_ibfk_1', 'T_affiliate', type_='foreignkey')
    op.drop_constraint('t_affiliate_ibfk_2', 'T_affiliate', type_='foreignkey')
    op.create_foreign_key(None, 'T_affiliate', 'T_bizdev', ['affiliate_enable'], ['bizdev_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key(None, 'T_affiliate', 'T_company', ['affiliate_company_id'], ['company_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_category_ibfk_1', 'T_category', type_='foreignkey')
    op.create_foreign_key(None, 'T_category', 'T_vertical', ['category_vertical_id'], ['vertical_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_contact_ibfk_1', 'T_contact', type_='foreignkey')
    op.create_foreign_key(None, 'T_contact', 'T_city', ['contact_zipcode'], ['city_zipcode'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_customer_ibfk_2', 'T_customer', type_='foreignkey')
    op.drop_constraint('t_customer_ibfk_1', 'T_customer', type_='foreignkey')
    op.create_foreign_key(None, 'T_customer', 'T_bizdev', ['customer_bizdev_id'], ['bizdev_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key(None, 'T_customer', 'T_company', ['customer_company_id'], ['company_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_constraint('t_lead_ibfk_2', 'T_lead', type_='foreignkey')
    op.drop_constraint('t_lead_ibfk_3', 'T_lead', type_='foreignkey')
    op.drop_constraint('t_lead_ibfk_1', 'T_lead', type_='foreignkey')
    op.create_foreign_key(None, 'T_lead', 'T_category', ['lead_category_id'], ['category_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key(None, 'T_lead', 'T_contact', ['lead_contact_id'], ['contact_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.create_foreign_key(None, 'T_lead', 'T_affiliate', ['lead_affiliate_id'], ['affiliate_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_constraint('t_modelcat_ibfk_1', 'T_modelcat', type_='foreignkey')
    op.create_foreign_key(None, 'T_modelcat', 'T_category', ['modelcat_category_id'], ['category_vertical_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_order_ibfk_1', 'T_order', type_='foreignkey')
    op.create_foreign_key(None, 'T_order', 'T_search', ['order_search_id'], ['search_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_sales_ibfk_2', 'T_sales', type_='foreignkey')
    op.drop_constraint('t_sales_ibfk_1', 'T_sales', type_='foreignkey')
    op.create_foreign_key(None, 'T_sales', 'T_order', ['sales_order_id'], ['order_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key(None, 'T_sales', 'T_lead', ['sales_lead_id'], ['lead_id'], source_schema='db_marketplace', referent_schema='db_marketplace', onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_constraint('t_search_ibfk_1', 'T_search', type_='foreignkey')
    op.create_foreign_key(None, 'T_search', 'T_user', ['search_user_id'], ['user_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_constraint('t_user_ibfk_2', 'T_user', type_='foreignkey')
    op.drop_constraint('t_user_ibfk_1', 'T_user', type_='foreignkey')
    op.create_foreign_key(None, 'T_user', 'T_company', ['user_company_id'], ['company_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.create_foreign_key(None, 'T_user', 'T_role', ['user_role_id'], ['role_id'], source_schema='db_marketplace', referent_schema='db_marketplace')
    op.drop_column('T_user', 'user_email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('T_user', sa.Column('user_email', mysql.VARCHAR(length=255), nullable=True))
    op.drop_constraint(None, 'T_user', schema='db_marketplace', type_='foreignkey')
    op.drop_constraint(None, 'T_user', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_user_ibfk_1', 'T_user', 'T_company', ['user_company_id'], ['company_id'])
    op.create_foreign_key('t_user_ibfk_2', 'T_user', 'T_role', ['user_role_id'], ['role_id'])
    op.drop_constraint(None, 'T_search', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_search_ibfk_1', 'T_search', 'T_user', ['search_user_id'], ['user_id'])
    op.drop_constraint(None, 'T_sales', schema='db_marketplace', type_='foreignkey')
    op.drop_constraint(None, 'T_sales', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_sales_ibfk_1', 'T_sales', 'T_order', ['sales_order_id'], ['order_id'])
    op.create_foreign_key('t_sales_ibfk_2', 'T_sales', 'T_lead', ['sales_lead_id'], ['lead_id'])
    op.drop_constraint(None, 'T_order', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_order_ibfk_1', 'T_order', 'T_search', ['order_search_id'], ['search_id'])
    op.drop_constraint(None, 'T_modelcat', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_modelcat_ibfk_1', 'T_modelcat', 'T_category', ['modelcat_category_id'], ['category_vertical_id'])
    op.drop_constraint(None, 'T_lead', schema='db_marketplace', type_='foreignkey')
    op.drop_constraint(None, 'T_lead', schema='db_marketplace', type_='foreignkey')
    op.drop_constraint(None, 'T_lead', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_lead_ibfk_1', 'T_lead', 'T_affiliate', ['lead_affiliate_id'], ['affiliate_id'])
    op.create_foreign_key('t_lead_ibfk_3', 'T_lead', 'T_category', ['lead_category_id'], ['category_id'])
    op.create_foreign_key('t_lead_ibfk_2', 'T_lead', 'T_contact', ['lead_contact_id'], ['contact_id'])
    op.drop_constraint(None, 'T_customer', schema='db_marketplace', type_='foreignkey')
    op.drop_constraint(None, 'T_customer', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_customer_ibfk_1', 'T_customer', 'T_company', ['customer_company_id'], ['company_id'])
    op.create_foreign_key('t_customer_ibfk_2', 'T_customer', 'T_bizdev', ['customer_bizdev_id'], ['bizdev_id'])
    op.drop_constraint(None, 'T_contact', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_contact_ibfk_1', 'T_contact', 'T_city', ['contact_zipcode'], ['city_zipcode'])
    op.drop_constraint(None, 'T_category', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_category_ibfk_1', 'T_category', 'T_vertical', ['category_vertical_id'], ['vertical_id'])
    op.drop_constraint(None, 'T_affiliate', schema='db_marketplace', type_='foreignkey')
    op.drop_constraint(None, 'T_affiliate', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_affiliate_ibfk_2', 'T_affiliate', 'T_company', ['affiliate_company_id'], ['company_id'])
    op.create_foreign_key('t_affiliate_ibfk_1', 'T_affiliate', 'T_bizdev', ['affiliate_enable'], ['bizdev_id'])
    op.drop_constraint(None, 'T_additoinalfield', schema='db_marketplace', type_='foreignkey')
    op.create_foreign_key('t_additoinalfield_ibfk_1', 'T_additoinalfield', 'T_lead', ['additoinalfield_lead_id'], ['lead_id'])
    # ### end Alembic commands ###

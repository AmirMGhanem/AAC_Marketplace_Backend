from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, JSON, String, TIMESTAMP, Table, text
from sqlalchemy.dialects.mysql import CHAR, INTEGER, LONGTEXT, MEDIUMTEXT, TIMESTAMP, TINYINT, VARCHAR
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBizdev(Base):
    __tablename__ = 'T_bizdev'
    __table_args__ = {'schema': 'db_marketplace'}

    bizdev_id = Column(Integer, primary_key=True)
    bizdev_name = Column(VARCHAR(255))
    bizdev_enable = Column(Integer)


class TRole(Base):
    __tablename__ = 'T_role'
    __table_args__ = {'schema': 'db_marketplace'}

    role_id = Column(Integer, primary_key=True)
    role_status = Column(String(255, 'utf8mb3_unicode_ci'))
    role_weight = Column(Integer)


class TState(Base):
    __tablename__ = 'T_state'
    __table_args__ = {'schema': 'db_marketplace'}

    state_id = Column(Integer, primary_key=True)
    state_name = Column(VARCHAR(50))
    state_code = Column(VARCHAR(2), nullable=False, index=True)
    state_timezone = Column(Integer)
    state_country_code = Column(CHAR(2))


class TVertical(Base):
    __tablename__ = 'T_vertical'
    __table_args__ = {'schema': 'db_marketplace'}

    vertical_id = Column(Integer, primary_key=True)
    vertical_name = Column(VARCHAR(255))


class TAffiliate(Base):
    __tablename__ = '_________________T_affiliate'
    __table_args__ = {'schema': 'db_marketplace'}

    affiliate_id = Column(Integer, primary_key=True)
    affiliate_shortname = Column(VARCHAR(255), nullable=False)
    affiliate_company_id = Column(Integer, index=True)
    affiliate_api_key = Column(VARCHAR(255))
    affiliate_api_password = Column(VARCHAR(255), comment='md5')
    affiliate_enable = Column(Integer, index=True)
    affiliate_bizdev_id = Column(Integer, index=True)
    affiliate_test = Column(Integer)
    affiliate_partnerid_AAC = Column(VARCHAR(255))


class TContact(Base):
    __tablename__ = '_________________T_contact'
    __table_args__ = {'schema': 'db_marketplace'}

    contact_id = Column(Integer, primary_key=True)
    contact_lastname = Column(VARCHAR(255))
    contact_firstname = Column(VARCHAR(255))
    contact_email = Column(VARCHAR(255))
    contact_phone = Column(VARCHAR(255))
    contact_address = Column(VARCHAR(255))
    contact_zipcode = Column(VARCHAR(255), index=True)


class TCustomer(Base):
    __tablename__ = '_________________T_customer'
    __table_args__ = {'schema': 'db_marketplace'}

    customer_id = Column(Integer, primary_key=True)
    customer_shortname = Column(VARCHAR(255))
    customer_company_id = Column(Integer, index=True)
    customer_enable = Column(Integer)
    customer_test = Column(Integer)
    customer_bizdev_id = Column(Integer, index=True)
    customer_critera = Column(JSON)
    customer_numclient_AAC = Column(Integer)


t__________________T_groupcat = Table(
    '_________________T_groupcat', metadata,
    Column('groupcat_id', INTEGER, nullable=False, unique=True),
    Column('groupcat_name', VARCHAR(100)),
    Column('groupcat_enable', TINYINT, server_default=text("'1'")),
    schema='db_marketplace'
)


class TModelcat(Base):
    __tablename__ = '_________________T_modelcat'
    __table_args__ = {'schema': 'db_marketplace'}

    modelcat_id = Column(Integer, nullable=False, unique=True)
    modelcat_category_id = Column(Integer, primary_key=True, nullable=False)
    modelcat_fieldname = Column(VARCHAR(50), primary_key=True, nullable=False)
    modelcat_field_sql = Column(VARCHAR(100), nullable=False)
    modelcat_fieldmaster = Column(VARCHAR(50))
    modelcat_pattern = Column(LONGTEXT, nullable=False)
    modelcat_description = Column(VARCHAR(500))
    ping_required = Column(VARCHAR(5), nullable=False)
    post_required = Column(VARCHAR(5), nullable=False)


class TCategory(Base):
    __tablename__ = 'T_category'
    __table_args__ = {'schema': 'db_marketplace'}

    category_id = Column(Integer, primary_key=True)
    category_vertical_id = Column(ForeignKey('db_marketplace.T_vertical.vertical_id', ondelete='SET NULL'), index=True, server_default=text("'1'"))
    category_name = Column(VARCHAR(255))
    category_enable = Column(Integer, server_default=text("'1'"))
    category_groupcat_id = Column(Integer, index=True)

    category_vertical = relationship('TVertical')


class TCity(Base):
    __tablename__ = 'T_city'
    __table_args__ = {'schema': 'db_marketplace'}

    city_id = Column(Integer, primary_key=True)
    city_zipcode = Column(VARCHAR(255), index=True)
    city_name = Column(VARCHAR(250))
    city_state_code = Column(ForeignKey('db_marketplace.T_state.state_code', ondelete='SET NULL'), index=True)
    city_lat = Column(Float)
    city_long = Column(Float)
    city_timezone = Column(Integer)
    city_country = Column(VARCHAR(5))
    city_area_code = Column(VARCHAR(75))
    city_population = Column(Integer)
    city_population_density = Column(Integer)
    city_median_home_value = Column(Integer)
    city_median_household_income = Column(Integer)
    city_radius_in_miles = Column(Integer)
    city_occupied_housing_units = Column(Integer)
    city_housing_units = Column(Integer)

    T_state = relationship('TState')


class TCompany(Base):
    __tablename__ = 'T_company'
    __table_args__ = {'schema': 'db_marketplace'}

    company_id = Column(Integer, primary_key=True)
    company_name = Column(VARCHAR(255))
    company_shortname = Column(String(255, 'utf8mb3_unicode_ci'))
    company_address1 = Column(VARCHAR(255))
    company_address2 = Column(VARCHAR(255))
    company_zipcode = Column(VARCHAR(255))
    company_city = Column(VARCHAR(255))
    company_country = Column(VARCHAR(255))
    company_ein = Column(VARCHAR(255))
    company_website = Column(VARCHAR(255))
    company_email = Column(VARCHAR(255))
    company_email_biz = Column(VARCHAR(255))
    company_email_tech = Column(VARCHAR(255))
    company_phone = Column(VARCHAR(255))
    company_bank_name = Column(VARCHAR(255))
    company_bank_routing = Column(VARCHAR(255))
    company_bank_account = Column(VARCHAR(255))
    company_bank_account_type = Column(VARCHAR(255))
    company_api_key = Column(String(255, 'utf8mb3_unicode_ci'))
    company_api_password = Column(String(255, 'utf8mb3_unicode_ci'))
    company_bizdev_id = Column(ForeignKey('db_marketplace.T_bizdev.bizdev_id'), index=True)
    company_test = Column(Integer, server_default=text("'0'"))
    company_active = Column(Integer, server_default=text("'1'"))
    company_AAC_partnerid = Column(VARCHAR(255))
    company_AAC_numclient = Column(VARCHAR(255))

    company_bizdev = relationship('TBizdev')


class TVerticalfield(Base):
    __tablename__ = 'T_verticalfield'
    __table_args__ = {'schema': 'db_marketplace'}

    verticalfields_id = Column(Integer, primary_key=True)
    verticalfields_vertical_id = Column(ForeignKey('db_marketplace.T_vertical.vertical_id', ondelete='SET NULL'), index=True)
    verticalfields_fieldname = Column(VARCHAR(50))
    verticalfields_field_sql = Column(VARCHAR(100))
    verticalfields_example = Column(VARCHAR(50))
    verticalfields_pattern = Column(LONGTEXT)
    verticalfields_description = Column(VARCHAR(500))
    verticalfields_mandatory = Column(Integer)
    verticalfields_vertical = relationship('TVertical')




class TAnswer(Base):
    __tablename__ = 'T_answer'
    __table_args__ = {'schema': 'db_marketplace'}

    answer_id = Column(Integer, primary_key=True)
    answer_verticalfield_id = Column(ForeignKey('db_marketplace.T_verticalfield.verticalfields_id'), nullable=False, index=True)
    answer_verticalfield_choice = Column(VARCHAR(255), nullable=False)
    answer_verticalfield_answer = Column(String(255, 'utf8mb3_unicode_ci'))

    answer_verticalfield = relationship('TVerticalfield',backref='answers')


class TLead(Base):
    __tablename__ = 'T_lead'
    __table_args__ = {'schema': 'db_marketplace'}

    lead_id = Column(Integer, primary_key=True)
    lead_category_id = Column(ForeignKey('db_marketplace.T_category.category_id', ondelete='SET NULL'), index=True)
    lead_company_id = Column(ForeignKey('db_marketplace.T_company.company_id', ondelete='SET NULL'), index=True)
    lead_partner_leadid = Column(VARCHAR(255))
    lead_company_subid = Column(VARCHAR(255))
    lead_quality_score = Column(Float(6))
    lead_comment = Column(VARCHAR(1000))
    lead_legs = Column(Integer)
    lead_timestamp = Column(TIMESTAMP(fsp=6), server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"))
    lead_ip = Column(DateTime)
    lead_trustedform = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_ULI = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_lastname = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_firstname = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_email = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_phone = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_address = Column(String(255, 'utf8mb3_unicode_ci'))
    lead_city_id = Column(ForeignKey('db_marketplace.T_city.city_id', ondelete='SET NULL'), index=True)
    lead_gender = Column(Integer)

    lead_category = relationship('TCategory')
    lead_city = relationship('TCity')
    lead_company = relationship('TCompany')


class TUser(Base):
    __tablename__ = 'T_user'
    __table_args__ = {'schema': 'db_marketplace'}

    user_id = Column(Integer, primary_key=True)
    user_name = Column(VARCHAR(255))
    user_company_id = Column(ForeignKey('db_marketplace.T_company.company_id'), index=True)
    user_login = Column(String(255, 'utf8mb3_unicode_ci'))
    user_password = Column(VARCHAR(255), comment='md5')
    user_role_id = Column(ForeignKey('db_marketplace.T_role.role_id'), index=True)

    user_company = relationship('TCompany')
    user_role = relationship('TRole')


class TAdditoinalfield(Base):
    __tablename__ = 'T_additoinalfield'
    __table_args__ = {'schema': 'db_marketplace'}

    additoinalfield_lead_id = Column(ForeignKey('db_marketplace.T_lead.lead_id'), primary_key=True, nullable=False)
    additoinalfield_fieldname = Column(VARCHAR(255), primary_key=True, nullable=False)
    additoinalfield_value = Column(VARCHAR(5000))
    additoinalfield_timestamp = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    additoinalfield_lead = relationship('TLead')


class TSearch(Base):
    __tablename__ = 'T_search'
    __table_args__ = {'schema': 'db_marketplace'}

    search_id = Column(Integer, primary_key=True)
    search_shortname = Column(VARCHAR(255))
    search_creaction_date = Column(DateTime)
    search_user_id = Column(ForeignKey('db_marketplace.T_user.user_id'), index=True)
    search_filter = Column(MEDIUMTEXT)
    search_infos = Column(MEDIUMTEXT)
    search_filter_files = Column(VARCHAR(3000))

    search_user = relationship('TUser')


class TOrder(Base):
    __tablename__ = 'T_order'
    __table_args__ = {'schema': 'db_marketplace'}

    order_id = Column(Integer, primary_key=True)
    order_search_id = Column(ForeignKey('db_marketplace.T_search.search_id'), index=True)
    order_enable = Column(Integer)
    order_creation_date = Column(DateTime)
    order_start_date = Column(DateTime)
    order_end_date = Column(DateTime)
    order_cpl = Column(Float(6))
    order_quantity = Column(Integer)
    order_criterias = Column(JSON)

    order_search = relationship('TSearch')


class TSale(Base):
    __tablename__ = 'T_sales'
    __table_args__ = {'schema': 'db_marketplace'}

    sales_id = Column(Integer, primary_key=True)
    sales_lead_id = Column(ForeignKey('db_marketplace.T_lead.lead_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    sales_order_id = Column(ForeignKey('db_marketplace.T_order.order_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    sales_price = Column(Float(10))
    sales_date = Column(DateTime)
    sales_return_customer = Column(Integer)

    sales_lead = relationship('TLead')
    sales_order = relationship('TOrder')
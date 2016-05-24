from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reservation = Table('reservation', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('guest', INTEGER),
    Column('table', INTEGER),
    Column('num_guests', INTEGER),
    Column('reservation_time', DATETIME),
)

reservation = Table('reservation', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('guest_id', Integer),
    Column('table_id', Integer),
    Column('num_guests', Integer),
    Column('reservation_time', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reservation'].columns['guest'].drop()
    pre_meta.tables['reservation'].columns['table'].drop()
    post_meta.tables['reservation'].columns['guest_id'].create()
    post_meta.tables['reservation'].columns['table_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reservation'].columns['guest'].create()
    pre_meta.tables['reservation'].columns['table'].create()
    post_meta.tables['reservation'].columns['guest_id'].drop()
    post_meta.tables['reservation'].columns['table_id'].drop()

from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
comment = Table('comment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('comment', String(length=10240)),
    Column('post_id', Integer),
)

post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('comment', VARCHAR(length=10240)),
    Column('category_id', INTEGER),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('post', String(length=64)),
    Column('category_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comment'].create()
    pre_meta.tables['post'].columns['comment'].drop()
    post_meta.tables['post'].columns['post'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comment'].drop()
    pre_meta.tables['post'].columns['comment'].create()
    post_meta.tables['post'].columns['post'].drop()

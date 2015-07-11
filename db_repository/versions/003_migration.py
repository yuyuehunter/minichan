from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('category_id', INTEGER),
    Column('post', VARCHAR(length=64)),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('text', String(length=10240)),
    Column('category_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['post'].drop()
    post_meta.tables['post'].columns['text'].create()
    post_meta.tables['post'].columns['title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['post'].create()
    post_meta.tables['post'].columns['text'].drop()
    post_meta.tables['post'].columns['title'].drop()

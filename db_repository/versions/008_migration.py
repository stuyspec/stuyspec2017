from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
article = Table('article', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('title', VARCHAR(length=256)),
    Column('section', VARCHAR(length=64)),
)

article = Table('article', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=256)),
    Column('content', Text),
    Column('timestamp', DateTime),
    Column('dept_id', Integer),
    Column('p_index', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=120)),
    Column('name', VARCHAR(length=64)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstName', String(length=128)),
    Column('lastName', String(length=128)),
    Column('username', String(length=128)),
    Column('password', String(length=128)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['article'].columns['body'].drop()
    pre_meta.tables['article'].columns['section'].drop()
    post_meta.tables['article'].columns['content'].create()
    post_meta.tables['article'].columns['dept_id'].create()
    post_meta.tables['article'].columns['p_index'].create()
    pre_meta.tables['user'].columns['name'].drop()
    post_meta.tables['user'].columns['firstName'].create()
    post_meta.tables['user'].columns['lastName'].create()
    post_meta.tables['user'].columns['password'].create()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['article'].columns['body'].create()
    pre_meta.tables['article'].columns['section'].create()
    post_meta.tables['article'].columns['content'].drop()
    post_meta.tables['article'].columns['dept_id'].drop()
    post_meta.tables['article'].columns['p_index'].drop()
    pre_meta.tables['user'].columns['name'].create()
    post_meta.tables['user'].columns['firstName'].drop()
    post_meta.tables['user'].columns['lastName'].drop()
    post_meta.tables['user'].columns['password'].drop()
    post_meta.tables['user'].columns['username'].drop()

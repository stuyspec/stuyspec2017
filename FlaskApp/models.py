# schema:
# https://docs.google.com/spreadsheets/d/181bJAbSEepuMjQyhE7dueGexzs7844WE2J2OrlgI3YY/edit?usp=sharing

UserArticle = Table('UserArticle',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
)

UserRole = Table('UserRole',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

ArticleTag = Table('ArticleTag',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128), index=True)
    lastName = db.Column(db.String(128), index=True)
    username = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    articles = relationship("Article",
        secondary=UserArticle,
        backref="users")    
    role = relationship("Role",
        secondary=UserRole,
        backref="users")
    media = relationship("Media", backref="user")

    def __repr__(self):
        return "<User (name='%s', id=%s, username='%s'>" % (
            self.firstName + self.lastName, str(self.id), self.username)


class Role(Base):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True)

    # backref: users

    def __repr__(self):
        return "<Role (title='%s')>" % ( self.title )


class Section(Base):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    description = db.Column(db.Text)
    articles = relationship("Article", backref="section")

    def __repr__(self):
        return "<Section (name='%s', id='%s')>" % (
            self.name, str(self.id) )


class Subsection(Base):
    __tablename__ = 'subsection'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    description = db.Column(db.Text)
    articles = relationship("Article", backref="subsection")

    def __repr__(self):
        return "<Subsection (name='%s', id='%s')>" % (
            self.name, str(self.id) )


class Article(Base):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    content = db.Column(db.Text)
    timestamp = db.Column(DateTime)
    p_index = db.Column(db.Integer)
    volume = db.Column(db.Integer, index=True) # need to multiple index
    issue = db.Column(db.Integer, index=True) # need to multiple index

    tags = relationship("Tag",
        secondary=ArticleTag,
        backref="articles")
    media = relationship("Media", backref="article")

    # backrefs: Users, Section, Subsection

    def __repr__(self):
        return "<Article (id=%s, title='%s')>" % (
            str(self.id), self.title )

"""
{
    'News': [
        'Campaign Coverage'
    ],
    'Opinions': [
        'Staff Editorial'
    ],
    'Features': [
        'September 11 Attacks',
        'College Essays',
        'VOICES'
    ],
    'Arts & Entertainment': [
        'Art',
        'Books',
        'Feature',
        'Film',
        'Food',
        'Music'
        'SING!',
        'STC',
        'Television',
        'Thinkpiece'
    ],
    'Humor': [
        'Disrespectator',
        'Spooktator'
    ],
    'Sports': [],
    'Photo': [
        'Photo Essay'
    ]
}
"""

class Tag(Base):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    # backref: Article

    def __repr__(self):
        return "<Tag (name='%s', id='%s')>" % (
            self.name, str(self.id) )


class Media(Base):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1024), unique=True)
    title = db.Column(db.String(128))
    caption = db.Column(db.Text)
    isFeatured = db.Column(db.Boolean)
    isPhoto = db.Column(db.Boolean)

    # backref: User, Article


class Advertisement(Base):
    __tablename__ = 'advertisement'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1024), unique=True)
    name = db.Column(db.String(128))
from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128), index=True)
    lastName = db.Column(db.String(128), index=True)
    username = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (str(self.id) + ": " + self.username)

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    dept_id = db.Column(db.Integer, index=True, unique=False) # this data type needs to be better
    p_index = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<Article %r>' % ( str(self.id) + ": " + self.title )

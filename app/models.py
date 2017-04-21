from app import db

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Tag(db.Model):
    tagID = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Tag %r>' % (self.text);

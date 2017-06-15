from FlaskAPI import db

# database diagram:
# https://docs.google.com/spreadsheets/d/181bJAbSEepuMjQyhE7dueGexzs7844WE2J2OrlgI3YY/edit?usp=sharing

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


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship("Article", back_populates="department")

    def __repr__(self):
        return '<Department %r>' % (self.name)

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    p_index = db.Column(db.Integer, index=True, unique=False)

    dept_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship("Department", back_populates="articles")

    def __repr__(self):
        return '<Article %r>' % ( str(self.id) + ": " + self.title )


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.auto_reload = True

db = SQLAlchemy(app)

from FlaskApp import views, models

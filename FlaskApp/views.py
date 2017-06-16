from flask import render_template
from FlaskApp import app, models
from sqlalchemy import desc
import sys
import datetime

"""
navbar:
0=default
1=collapsed
2=shade
"""

@app.route('/')
@app.route('/index')
def index():
    articles = models.Article.query.all()#order_by(desc(models.Article.timestamp))
    articleProperties = models.Article.__table__.columns
    users = models.User.query.all()#order_by(models.User.username)
    userProperties = models.User.__table__.columns
    return render_template("index.html",
                           title="Stuyvesant Spectator",
                           navType=0,
                           articles=articles,
                           articleProperties=articleProperties,
                           users=users,
                           userProperties=userProperties)

@app.route('/article/<int:article_id>')
def article_test(article_id):
    a = models.Article.query.get(article_id)

    if a is None:
        return render_template('404.html',
                               title="404 Error",
                               navType=0
        ), 404
    else:
        paragraphs = a.content.split('\n')
        paragraphs[0] = "<dc>" + paragraphs[0][0] + "</dc>" + paragraphs[0][1:]

    return render_template("article.html",
                           paragraphs=paragraphs,
                           title="Article",
                           navType=1,
                           article=a
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
                           title="404 Error",
                           navType=0
    ), 404

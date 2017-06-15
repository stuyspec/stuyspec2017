from flask import render_template
from app import app, db, models
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
    return render_template("index.html",
                           title="Stuyvesant Spectator",
                           navType=0,
                           articles=models.Article.query.all(),
                           users=models.User.query.all())

@app.route('/article')
def article_default():
    article(4)

@app.route('/article/<int:article_id>')
def article(article_id):
    a = models.Article.query.get(article_id)

    paragraphs = a.content.split('\n')
    paragraphs[0] = "<dc>" + paragraphs[0][0] + "</dc>" + paragraphs[0][1:]

    return render_template("article.html",
                           paragraphs=paragraphs,
                           title="Article",
                           navType=1,
                           article=a)






@app.route('/the_week')
def the_week():
    return render_template("the_week.html",
                           title="9/11",
                           navbar=2)
@app.route('/feed_rail')
def goings_on():
    return render_template("feed_rail.html",
                           title="Feed Rail",
                           navbar=1)
@app.route('/antarctica')
def antarctica():
    return render_template("antarctica.html",
                           title="Antarctica",
                           navbar=2)
@app.route('/fat_text')
def fat_text():
    return render_template("fat_text.html",
                           title="Thesis & Background",
                           navbar=3)
@app.route('/tall_text')
def tall_text():
    return render_template("tall_text.html",
                           title="Charlie Did It")

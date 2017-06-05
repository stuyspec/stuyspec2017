from flask import render_template
from app import app, db, models
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
    posts = [
        {
            'timestamp': '2017-04-15 09:41:03',
            'articleID': 106,
            'title': 'New York',
            'authors': [
                {'name': 'George Zheng'},
                {'name': 'Jason Kao'},
            ],
            'body': 'Beautiful day in New York!',
            'viewcount': 6,
            'tags': [3, 4, 2, 1, 5]
        },
        {
            'timestamp': '2017-04-15 09:49:03',
            'articleID': 109,
            'title': 'Stuyvesant!',
            'authors': [
                {'name': 'Sabrina Wen'},
                {'name': 'Angela Tom'},
            ],
            'body': 'Stuyvesant High School provides excellent education.',
            'viewcount': 10,
            'tags': [9, 10, 0, 34, 2]
        },
        {
            'timestamp': '2017-04-15 09:49:03',
            'articleID': 109,
            'title': 'Stuyvesant!',
            'authors': [
                {'name': 'Sabrina Wen'},
                {'name': 'Angela Tom'},
            ],
            'body': 'Stuyvesant High School provides excellent education.',
            'viewcount': 10,
            'tags': [9, 10, 0, 34, 2]
        },
        {
            'timestamp': '2017-04-15 09:49:03',
            'articleID': 109,
            'title': 'Stuyvesant!',
            'authors': [
                {'name': 'Sabrina Wen'},
                {'name': 'Angela Tom'},
            ],
            'body': 'Stuyvesant High School provides excellent education.',
            'viewcount': 10,
            'tags': [9, 10, 0, 34, 2]
        }
    ]
    return render_template("index.html",
                           title="Stuyvesant Spectator",
                           navbar=0,
                           posts=posts)


@app.route('/article')
def article():
    return render_template("article.html",
                           title="Article",
                           navbar=1)

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

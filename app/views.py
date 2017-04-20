from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'name': 'Haley Cain'}
    navigation_bar = [
        {
            '/news': {		
                'id': 0
            },
            '/opinions': {
                'id': 1
            },
            '/humor': {
                'id': 2
            },
            '/features': {
                'id': 3
            },
            '/ae': {
                'id': 4
            },
            '/sports': {
                'id': 5
            }
        }
    ]
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
        }
    ]

    return render_template("index.html",
                           user=user,
                           posts=posts,
                           navigation_bar=navigation_bar)


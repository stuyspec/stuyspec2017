from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__) # helps flask find root path

@app.route('/') # decoratee runs when app routes to '/'
def index():
    return render_template("header.html")

@app.route('/login/', methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route('/news/<title>')
def show_ae(title):
    return "news: " + title

if __name__ == '__main__': # only runs app if this script is run directly (main file), bc some files may be imported
    app.run(debug=True)

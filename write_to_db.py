from FlaskApp import models, db
import datetime
import sys
import codecs

def write_article(title, content_filename, dept_id):
    with codecs.open(content_filename, 'r', 'utf-8') as content_file:
        a = models.Article(title=title.replace('_',' '),
                           content=content_file.read(),
                           timestamp=datetime.datetime.utcnow(),
                           dept_id=dept_id,
                           p_index=0)
        db.session.add(a)
        db.session.commit()
        print("Successfully wrote Article " + title.replace('_',' ') + ".")

def delete_article():
    print("Current articles: " + str(models.Article.query.all()))
    article_id = int(raw_input("Which article to delete? "))
    a = models.Article.query.get(article_id)
    if a is None:
        print("No article has id " + str(article_id) + ".")
        sys.exit()
    confirmation = str(raw_input("Delete article " + str(a) + "? (y/n) "))
    if confirmation == "y":
        db.session.delete(a)
    else:
        print("Thanks for saving " + str(a) + "!")
        sys.exit()
    db.session.commit()
    print("Successfully deleted Article " + str(a))

def delete_all_articles():
    articles = models.Article.query.all()
    print("Current articles: " + str(articles))
    confirmation = str(raw_input("Delete all articles? (y/n) "))
    if confirmation == "y":
        for a in articles:
            db.session.delete(a)
    else:
        print("Deleting aborted.")
        sys.exit()
    db.session.commit()
    print("Deleted all articles.")

def write_user(first, last, uname, pword, email):
    u = models.User(firstName=first,
                    lastName=last,
                    username=uname,
                    password=pword,
                    email=email)
    db.session.add(u)
    db.session.commit()
    print("Successfully wrote User " + first + " " + last + ".")

def delete_user():
    print("Current users: " + str(models.User.query.all()))
    user_id = input("Which user to delete? ")
    u = models.Article.query.get(user_id)
    if a is None:
        print("No user has id " + str(user_id) + ".")
        sys.exit()
    confirmation = input("Delete user " + str(u) + "? (y/n) ")
    if confirmation == "":
        db.session.delete(u)
    else:
        print("Thanks for saving " + str(u) + "!")
        sys.exit()
    db.session.commit()
    print("Successfully deleted User " + str(u))

def delete_all_users():
    users = db.session.query(models.User).all()
    print("Current articles: " + str(users))
    confirmation = str(raw_input("Delete all users? (y/n) "))
    if confirmation == "y":
        for a in users:
            db.session.delete(a)
    else:
        print("Deleting aborted.")
        sys.exit()
    db.session.commit()
    print("Deleted all users.")

if __name__ == "__main__":
    if sys.argv[1] == 'user':
        write_user( sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6] )
    elif sys.argv[1] == 'article':
        write_article( sys.argv[2], sys.argv[3], sys.argv[4] )
    elif sys.argv[1] == 'delete':
        if sys.argv[2] == 'user':
            delete_user()
        elif sys.argv[2] == 'article':
            delete_article()
        elif sys.argv[2] == 'all':
            if sys.argv[3] == 'users':
                delete_all_users()
            elif sys.argv[3] == 'articles':
                delete_all_articles()
    elif sys.argv[1] == 'update':
        if sys.argv[2] == 'user':
            update_user()
        elif sys.argv[2] == 'article':
            update_article()
    else:
        print("First argument must be article or user.")

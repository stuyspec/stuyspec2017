#!flask/bin/python
from FlaskApp import app

# This will run the application, change the debug do deliminate the nice error messages (every error would then result in an error 404 message)
if __name__ == "__main__":
    app.run(debug = True) # Can change back debug

import functools

from flask import flash, redirect, session

from app import app, models, db
import hashlib

def authenticate(permission_to_check):
    def auth(f0):
        @functools.wraps(f0)
        def wrapper(*args, **kwargs):
            if not 'username' in session:
                flash('You are not logged in')
                return redirect('index0')
            
            user = models.User.query.filter_by(username = session['username']).first()
            
            if not user:
                flash('You are not logged in')
                return redirect('index0')
            
            if user.check_permission(permission_to_check):
                return f0(*args, **kwargs)
            flash('You do not have permission to view this page')
            return redirect('index0')
        return wrapper
    return auth

def get_user():
    if not 'username' in session:
        return None
    return models.User.query.filter_by(username = session['username']).first()


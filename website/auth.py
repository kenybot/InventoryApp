from flask import Blueprint,render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logut():
    return "<p> THIS IS THE LOGOUT </p>"

@auth.route('/sign-up')
def signup():
    return render_template('signup.html')
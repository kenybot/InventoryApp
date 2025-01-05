#url endpoints for the functioning website
#store standard routes for the website
from flask import Blueprint, render_template

view = Blueprint('view', __name__)

#define a route
@view.route('/')
def home():
    return render_template("home.html")
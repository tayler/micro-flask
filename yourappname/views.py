# This is where the routes are defined. It may be split into
# a package of its own (yourapp/views/) with related views grouped together
# into modules.
from flask import Blueprint, render_template

# this Blueprint is registered in this module's __init__.py
public = Blueprint('public', __name__)

@public.route('/')
def home():
    return render_template('home.html')

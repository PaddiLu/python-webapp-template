"""
Module defining URL paths for a flask app
and for rendering content.
"""

# Imports
from flask import Blueprint, render_template

# Constants
_BLUEPRINT_NAME = 'pages'
_STATIC_ENDPOINT = _BLUEPRINT_NAME + '.static'

# Routes
pages = Blueprint(_BLUEPRINT_NAME, __name__,
                  template_folder='templates',
                  static_folder='../static',
                  static_url_path='/static')

@pages.route('/index')
@pages.route('/')
def index():
    return render_template('index.html.j2', static = _STATIC_ENDPOINT)

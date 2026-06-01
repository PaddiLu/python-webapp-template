"""
Module defining URL paths for a flask app
and for rendering content.
"""

# Imports
from flask import Blueprint, render_template, request

from . import paths

# Constants
_BLUEPRINT_NAME = 'pages'
_STATIC_ENDPOINT = _BLUEPRINT_NAME + '.static'

# Routes
pages = Blueprint(_BLUEPRINT_NAME, __name__,
                  template_folder=paths.TEMPLATES,
                  static_folder=paths.STATIC,
                  static_url_path='/static')

_CONTEXT = {
    # Values to be passed to all templates
    'static': _STATIC_ENDPOINT
}

@pages.route('/index', methods=['GET','POST'])
@pages.route('/', methods=['GET','POST'])
def index():
    name = request.form['name'] if request.method == 'POST' else '' 
    return render_template('index.html.j2', **_CONTEXT, name = name)

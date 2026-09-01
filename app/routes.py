"""
Module defining URL paths for a flask app
and for rendering content.
"""


# Imports
import flask

from . import const
from . import paths


# Constants
_BLUEPRINT_NAME = 'pages'
_STATIC_ENDPOINT = _BLUEPRINT_NAME + '.static'

_BLUEPRINT_CONTEXT = {
    'app': const.app,
    'static': _STATIC_ENDPOINT,
}


# Blueprints
pages = flask.Blueprint(
    _BLUEPRINT_NAME, __name__,
    template_folder=paths.TEMPLATES,
    static_folder=paths.STATIC,
    static_url_path='/static',
)
pages.context_processor(lambda : _BLUEPRINT_CONTEXT)

# Routes
@pages.route('/index')
@pages.route('/')
def index():
    return flask.render_template('base.html.j2')

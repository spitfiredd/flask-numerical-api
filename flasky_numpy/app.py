from flask import Flask

from .extensions import db, guard, cors
from .model import User


def create_app(config='flasky_numpy.settings'):
    app = Flask(__name__)
    app.config.from_object(config)

    load_extension(app)
    register_blueprints(app)
    register_shellcontext(app)

    return app


def load_extension(app):
    """ Register Extensions. """
    db.init_app(app)
    guard.init_app(app, User)
    cors.init_app(app)
    return None


def register_blueprints(app):
    """ Register Blueprints. """
    from .views import api_bp, API_VERSION_V1
    from .login import login_bp

    app.register_blueprint(
        api_bp,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1
        )
    )

    app.register_blueprint(login_bp)
    return None


def register_shellcontext(app):
    """Register shell context objects. Use Shell to create dummy user"""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': User,
            'guard': guard
        }

    app.shell_context_processor(shell_context)
    return None

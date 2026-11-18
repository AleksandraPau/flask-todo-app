from configs import config
from controllers import blueprints
from flask import Flask


def create_app(config_name=None):
    if config_name is None:
        config_name = "default"

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app

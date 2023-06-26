from flask import Flask

from application.rest import pb_renko_create


def create_app(config_name):
    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(pb_renko_create.blueprint)

    return app

from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import dog_bp
    app.register_blueprint(dog_bp)

    return app

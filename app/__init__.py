from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import dog_bp
    app.register_blueprint(dog_bp)

    from .routes import cat_bp
    app.register_blueprint(cat_bp)
    return app

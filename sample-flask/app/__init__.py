from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Redis URL
    app.config['RQ_REDIS_URL'] = os.getenv('REDIS_URL')

    # RQ
    from jobs import rq
    rq.init_app(app)

    # Blueprints
    from routes import default_blueprint
    app.register_blueprint(default_blueprint)

    return app

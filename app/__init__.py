from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
        FROM_EMAIL=os.environ.get('FROM_EMAIL')
    )

    from . import portfolio
    
    app.register_blueprint(portfolio.bp)
    

    return app
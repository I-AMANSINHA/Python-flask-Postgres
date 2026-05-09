import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import os
import logging
from flask import Flask
from config import Config
from extensions import db
from routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Logging Setup
    if not os.path.exists('logs'): os.makedirs('logs')
    logging.basicConfig(filename='logs/api.log', level=logging.INFO, 
                        format='%(asctime)s %(levelname)s: %(message)s')

    # Initialize Database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register Routes
    app.register_blueprint(main)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    @app.route("/")
    def home():
        return "Hello World"
    
    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from config import db, migrate
from routes.User import user_bp
from routes.Login import login_bp  # Importamos la nueva ruta de login
from models import User

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Leo222310400@examenapi.chy4csmq0erk.us-east-2.rds.amazonaws.com/Examen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)
migrate.init_app(app, db)

# Registrar blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(login_bp) 

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from database import db
from models import Usuario

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'API conectada a base de datos con modelo Usuario'

if __name__ == '__main__':
    app.run(debug=True)

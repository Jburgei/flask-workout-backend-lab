from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from server.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)
#testing route
@app.route('/')
def home():
    return {"message": "Workout API is running!"}, 200

if __name__ == '__main__':
    app.run(port =5555, debug=True)
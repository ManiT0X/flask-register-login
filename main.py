from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_wtf import CSRFProtect
from datetime import datetime
from blueprints.user import user
from blueprints.index import index


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisIsNotVerySecure'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
CSRFProtect(app)


app.register_blueprint(user)
app.register_blueprint(index)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Users, int(user_id))


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    creation_date = db.Column(db.Date, default=datetime.now().date())
    creation_time = db.Column(db.String(20))
    role = db.Column(db.String(25), nullable=False)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(100))
    date = db.Column(db.Date, default=datetime.now().date())
    time = db.Column(db.String(20))
    status = db.Column(db.String(30))


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

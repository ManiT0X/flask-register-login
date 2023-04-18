from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        from main import app, db, Users, Log
        with app.app_context():
            email = request.form.get('email')
            password = request.form.get('password')
            user_ = Users.query.filter_by(email=email).first()
            if user_:
                if check_password_hash(user_.password, password):
                    login_user(user_)
                    new_log = Log(email=email, status='success', time=str(datetime.now().time()))
                    db.session.add(new_log)
                    db.session.commit()
                    return {"status": "logged in"}, 200
                new_log = Log(email=email, status='fail: wrong password', time=str(datetime.now().time()))
                db.session.add(new_log)
                db.session.commit()
                return {"error": "wrong password"}, 409
            new_log = Log(email=email, status='fail: wrong email', time=str(datetime.now().time()))
            db.session.add(new_log)
            db.session.commit()
            return {"error": "email is not registered"}, 409
    return render_template('login.html')


# noinspection PyArgumentList
@user.route('/register', methods=['GET', 'POST'])
def register():
    if not current_user.is_authenticated:
        if request.method == 'POST':
            from main import app, db, Users, Log
            with app.app_context():
                username = request.form.get('username')
                email = request.form.get('email')
                password = request.form.get('password')
                if Users.query.filter_by(email=email).first():
                    return {"error": "this email is registered"}, 409
                elif Users.query.filter_by(username=username).first():
                    return {"error": "this username is taken"}, 409
                else:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=8),
                        role='user',
                        creation_time=str(datetime.now().time())
                    )
                    db.session.add(new_user)
                    db.session.commit()
                    return {"status": "logged in"}, 200
        return render_template('register.html')
    return redirect(url_for('index.profile'))


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', current_user=current_user)
    return redirect(url_for('user.login'))

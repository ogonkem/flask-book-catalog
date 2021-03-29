from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import User
from datetime import datetime

@at.context_processor
def inject_now():
    return dict(now=datetime.utcnow())

@at.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit(): # rather than 'if request.method == 'POST':'
        User.create_user(
          user=form.name.data,
          email=form.email.data,
          password=form.password.data)
        flash('Registration Successfull')
        return redirect(url_for('authentication.user_login'))
    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))
    form = LoginForm()
    if form.validate_on_submit(): # rather than 'if request.method == 'POST':'
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.user_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html', form=form)

    
@at.route('/logout')
@login_required
def user_logout():
    logout_user()
    return redirect(url_for('main.display_books'))
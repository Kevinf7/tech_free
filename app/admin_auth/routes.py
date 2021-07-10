from flask import render_template, redirect, url_for, flash, request, session
from flask_login import current_user, login_user, logout_user, login_required
from app import db, login_manager
from app.admin_auth import bp
from app.admin_auth.forms import LoginForm, RegistrationForm, ResetPasswordForm, ForgotPasswordForm
from app.admin_auth.email import send_password_reset_email
from app.admin_auth.models import User
from werkzeug.urls import url_parse
from datetime import datetime


# ADMIN AUTH routes

@bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_main.index'))
    next_page = request.args.get('next')
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password','danger')
            return redirect(url_for('admin_auth.login',next=next_page))

        login_user(user, remember=form.remember_me.data)
        user.last_seen = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        flash('You are now logged in','success')

        # in case url is absolute we will ignore, we only want a relative url
        # netloc returns the www.website.com part
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('admin_main.index'))
        return redirect(url_for(next_page))

    return render_template('admin_auth/login.html',form=form)


@bp.route('/logout')
@login_required
def logout():
    session.pop('edit_post',None)
    logout_user()
    flash('You are now logged out','success')
    return redirect(url_for('admin_auth.login'))


@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin_auth.login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, firstname=form.firstname.data, \
                    lastname=form.lastname.data, )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!','success')
        return redirect(url_for('admin_auth.login'))
    return render_template('admin_auth/register.html', form=form)


@bp.route('/forgot_password',methods=['GET','POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('admin_auth.login'))
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if not send_password_reset_email(user):
                flash('Sorry system error','danger')
        flash('Check your email for instructions to reset your password','success')
    return render_template('admin_auth/forgot_password.html',form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('admin_auth.login'))
    user = User.verify_reset_password_token(token)
    if not user:
        flash('Token has expired or is no longer valid','danger')
        return redirect(url_for('admin_auth.login'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset','success')
        return redirect(url_for('admin_auth.login'))
    return render_template('admin_auth/reset_password.html', form=form)


# handler when you are trying to access a page but you are not logged in
@login_manager.unauthorized_handler
def unauthorized():
    #flash('You must be logged in to view this page.','danger')
    return redirect(url_for('admin_auth.login',next=request.endpoint))


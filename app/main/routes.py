from flask import render_template, request, redirect, url_for, flash
from app.main import bp
from app import db
from app.admin_message.models import Message


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    if not name or not email:
        flash('Name and email are mandatory','danger')
        return redirect(url_for('main.index'))

    msg = Message(name=name, email=email, phone=phone, message=message)
    db.session.add(msg)
    db.session.commit()
    flash('Message has been sent','success')
    return redirect(url_for('main.index'))



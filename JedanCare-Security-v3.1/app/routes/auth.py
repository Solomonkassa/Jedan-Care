from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db 
from app.models import User, Doctor, Admin
from app.forms import UserLoginForm, DoctorLoginForm, AdminLoginForm, AdminRegistrationForm, DoctorRegistrationForm, UserRegistrationForm
from app.routes import auth_bp

@auth_bp.route('/login/user', methods=['GET', 'POST'])
def user_login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('user_login.html', form=form)

@auth_bp.route('/login/doctor', methods=['GET', 'POST'])
def doctor_login():
    form = DoctorLoginForm()
    if form.validate_on_submit():
        doctor = Doctor.query.filter_by(email=form.email.data).first()
        if doctor and check_password_hash(doctor.password_hash, form.password.data):
            login_user(doctor)
            flash('Login successful', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('doctor_login.html', form=form)

@auth_bp.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and check_password_hash(admin.password_hash, form.password.data):
            login_user(admin)
            flash('Login successful', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('admin_login.html', form=form)

@auth_bp.route('/signup/user', methods=['GET', 'POST'])
def user_signup():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('User registration successful', 'success')
        return redirect(url_for('auth.user_login'))
    return render_template('user_signup.html', form=form)

@auth_bp.route('/signup/doctor', methods=['GET', 'POST'])
def doctor_signup():
    form = DoctorRegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_doctor = Doctor(name=form.name.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_doctor)
        db.session.commit()
        flash('Doctor registration successful', 'success')
        return redirect(url_for('auth.doctor_login'))
    return render_template('doctor_signup.html', form=form)

@auth_bp.route('/signup/admin', methods=['GET', 'POST'])
def admin_signup():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_admin = Admin(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        flash('Admin registration successful', 'success')
        return redirect(url_for('auth.admin_login'))
    return render_template('admin_signup.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful', 'success')
    return redirect(url_for('main.home'))

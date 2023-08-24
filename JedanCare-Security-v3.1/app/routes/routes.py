from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app.forms import ContactForm, AppointmentForm
from app.models import Contact, Appointment, User, Doctor, Admin
from app.routes import main_bp
from app import db
# Add your routes for contact forms, appointments, admin, user, and doctors here
# For example:

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, email=form.email.data, subject=form.subject.data, message=form.message.data)
        # Save the contact data to the database
        flash('Contact form submitted', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', form=form)

@main_bp.route('/appointment', methods=['GET', 'POST'])
@login_required
def appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(name=form.name.data, email=form.email.data, phone=form.phone.data, doctor_id=form.doctor_id.data, message=form.message.data)
        # Save the appointment data to the database
        flash('Appointment scheduled', 'success')
        return redirect(url_for('main.appointment'))
    return render_template('appointment.html', form=form)

# Implement routes for admin, user, and doctor operations

@main_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if isinstance(current_user, Admin):
        contacts = Contact.query.all()
        appointments = Appointment.query.all()
        users = User.query.all()
        doctors = Doctor.query.all()
        return render_template('admin_dashboard.html', contacts=contacts, appointments=appointments, users=users, doctors=doctors)
    else:
        flash('You do not have permission to access this page', 'danger')
        return redirect(url_for('main.home'))

@main_bp.route('/user/profile')
@login_required
def user_profile():
    if isinstance(current_user, User):
        return render_template('user_profile.html', user=current_user)
    else:
        flash('You do not have permission to access this page', 'danger')
        return redirect(url_for('main.home'))

@main_bp.route('/doctor/profile/<int:doctor_id>')
@login_required
def doctor_profile(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    if isinstance(current_user, Doctor) and current_user.id == doctor_id:
        return render_template('doctor_profile.html', doctor=doctor)
    else:
        flash('You do not have permission to access this page', 'danger')
        return redirect(url_for('main.home'))

@main_bp.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    if isinstance(current_user, Admin):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully', 'success')
    else:
        flash('You do not have permission to perform this action', 'danger')
    return redirect(url_for('main.admin_dashboard'))

@main_bp.route('/admin/delete_doctor/<int:doctor_id>', methods=['POST'])
@login_required
def admin_delete_doctor(doctor_id):
    if isinstance(current_user, Admin):
        doctor = Doctor.query.get_or_404(doctor_id)
        db.session.delete(doctor)
        db.session.commit()
        flash('Doctor deleted successfully', 'success')
    else:
        flash('You do not have permission to perform this action', 'danger')
    return redirect(url_for('main.admin_dashboard'))

@main_bp.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_user(user_id):
    if isinstance(current_user, Admin):
        user = User.query.get_or_404(user_id)
        if request.method == 'POST':
            # Update user details based on form data
            user.username = request.form.get('username')
            user.email = request.form.get('email')
            # Update other user attributes
            db.session.commit()
            flash('User details updated successfully', 'success')
            return redirect(url_for('main.admin_dashboard'))
        return render_template('admin_edit_user.html', user=user)
    else:
        flash('You do not have permission to perform this action', 'danger')
        return redirect(url_for('main.admin_dashboard'))

# ... Additional CRUD operations ...


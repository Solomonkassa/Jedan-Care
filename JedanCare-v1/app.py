from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    doctors = db.relationship('Doctor', backref='department', lazy=True)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    message = db.Column(db.Text)

@app.route('/')
def home():
    return render_template('appointments.html')

@app.route('/get_doctors/<int:department_id>', methods=['GET'])
def get_doctors(department_id):
    doctors = Doctor.query.filter_by(department_id=department_id).all()
    doctors_data = [{'id': doctor.id, 'name': doctor.name} for doctor in doctors]
    return jsonify(doctors_data)

@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = datetime.strptime(request.form['date'], '%Y-%m-%dT%H:%M')  # Updated format for datetime-local input
        doctor_id = request.form['doctor']
        message = request.form['message']

        new_appointment = Appointment(name=name, email=email, phone=phone, date=date, doctor_id=doctor_id, message=message)
        db.session.add(new_appointment)
        db.session.commit()
        flash('Appointment successfully scheduled!', 'success')
        return redirect(url_for('appointments'))

    departments = Department.query.all()
    doctors = Doctor.query.all()
    return render_template('appointments.html', departments=departments, doctors=doctors)

@app.route('/admin/update_doctor/<int:doctor_id>', methods=['GET', 'POST'])
def update_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    
    if request.method == 'POST':
        doctor.name = request.form['name']
        db.session.commit()
        flash('Doctor updated successfully!', 'success')
        return redirect(url_for('admin'))
    
    return render_template('update_doctor.html', doctor=doctor)

@app.route('/admin/delete_doctor/<int:doctor_id>', methods=['POST'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    db.session.delete(doctor)
    db.session.commit()
    flash('Doctor deleted successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/update_department/<int:department_id>', methods=['GET', 'POST'])
def update_department(department_id):
    department = Department.query.get_or_404(department_id)
    
    if request.method == 'POST':
        department.name = request.form['name']
        db.session.commit()
        flash('Department updated successfully!', 'success')
        return redirect(url_for('admin'))
    
    return render_template('update_department.html', department=department)

@app.route('/admin/delete_department/<int:department_id>', methods=['POST'])
def delete_department(department_id):
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    flash('Department deleted successfully!', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Check if sample departments exist
        cardiology = Department.query.filter_by(name='Cardiology').first()
        orthopedics = Department.query.filter_by(name='Orthopedics').first()

        if not cardiology:
            cardiology = Department(name='Cardiology')
            db.session.add(cardiology)

        if not orthopedics:
            orthopedics = Department(name='Orthopedics')
            db.session.add(orthopedics)

        # Check if sample doctors exist
        doctor1 = Doctor.query.filter_by(name='Dr. John Doe').first()
        doctor2 = Doctor.query.filter_by(name='Dr. Jane Smith').first()

        if not doctor1:
            doctor1 = Doctor(name='Dr. John Doe', department=cardiology)
            db.session.add(doctor1)

        if not doctor2:
            doctor2 = Doctor(name='Dr. Jane Smith', department=orthopedics)
            db.session.add(doctor2)

        db.session.commit()

        # Check if sample appointment exists
        appointment = Appointment.query.filter_by(name='John Doe Appointment').first()

        if not appointment:
            appointment = Appointment(
                name='John Doe Appointment',
                email='john@example.com',
                phone='123-456-7890',
                date=datetime.utcnow(),
                doctor=doctor1,
                message='Sample appointment message'
            )
            db.session.add(appointment)

        db.session.commit()

        app.run(debug=True)


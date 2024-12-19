from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/appointments')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models import Doctor, Appointment

@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.json
    doctor = Doctor(name=data['name'], specialization=data['specialization'], availability=data['availability'])
    db.session.add(doctor)
    db.session.commit()
    return jsonify({"message": "Doctor profile created successfully."}), 201

@app.route('/appointments', methods=['POST'])
def book_appointment():
    data = request.json
    appointment = Appointment(patient_name=data['patient_name'], doctor_id=data['doctor_id'], appointment_time=data['appointment_time'])
    db.session.add(appointment)
    db.session.commit()
    return jsonify({"message": "Appointment booked successfully."}), 201

@app.route('/appointments/<int:doctor_id>', methods=['GET'])
def view_appointments(doctor_id):
    appointments = Appointment.query.filter_by(doctor_id=doctor_id).all()
    return jsonify([{
        "patient_name": a.patient_name,
        "appointment_time": a.appointment_time.strftime('%Y-%m-%d %H:%M')
    } for a in appointments])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

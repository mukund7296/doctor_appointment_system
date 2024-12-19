# Doctor Appointment Management System

This project is a Flask-based application for managing doctor appointments. It uses Docker for containerization and PostgreSQL as the database backend.

## Features
- **Create Doctor Profiles**
- **Book Appointments**
- **View Booked Appointments**

## Getting Started
### Prerequisites
- Docker and Docker Compose

### Installation
1. Clone the repository.
2. Run `docker-compose up` to start the system.

### Endpoints
- `POST /doctors`: Add doctor profiles.
- `POST /appointments`: Book appointments.
- `GET /appointments/<doctor_id>`: View appointments for a doctor.

CRM Backend Project - README.md
# CRM Backend Project

A complete Django REST Framework based CRM (Customer Relationship Management) backend system.

This project provides APIs for:

- User Authentication
- Complaint Management
- Notifications
- Reports & Analytics
- Role-based Access
- JWT Authentication
- PostgreSQL / SQLite Support

---

# Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- SQLite
- JWT Authentication
- Pandas
- NumPy
- Docker
- AWS EC2

---

# Project Structure

crm_project/
│
├── accounts/
├── complaints/
├── notifications/
├── reports/
├── crm_project/
├── manage.py
├── requirements.txt
├── Dockerfile
└── db.sqlite3

---

# Features

## Authentication System
- User Registration
- User Login
- JWT Token Authentication
- Protected APIs

## Complaint Management
- Create Complaint
- View Complaints
- Update Complaint Status
- Delete Complaint
- Complaint Tracking

## Notifications
- Send Notifications
- View Notifications

## Reports
- Complaint Analytics
- Monthly Reports
- Status Reports

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/subhan2001/crm-backend-project.git
cd crm-backend-project
Create Virtual Environment
Windows
python -m venv crmvenv
crmvenv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Database Configuration
SQLite (Easy Setup)

In settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
PostgreSQL Configuration

Install PostgreSQL and update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Run Migrations
python manage.py makemigrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser
Run Development Server
python manage.py runserver

Server URL:

http://127.0.0.1:8000
JWT Authentication APIs
Register User
Endpoint
POST /api/accounts/register/
Purpose

Creates a new user account.

Request Body
{
    "username": "subhan",
    "email": "subhan@gmail.com",
    "password": "password123"
}
Login User
Endpoint
POST /api/accounts/login/
Purpose

Authenticates user and returns JWT tokens.

Request Body
{
    "username": "subhan",
    "password": "password123"
}
Response
{
    "refresh": "token",
    "access": "token"
}
Complaints APIs
Create Complaint
Endpoint
POST /api/complaints/create/
Purpose

Creates a new complaint.

Request Body
{
    "title": "Network Issue",
    "description": "Internet not working"
}
Get All Complaints
Endpoint
GET /api/complaints/
Purpose

Returns all complaints.

Get Complaint By ID
Endpoint
GET /api/complaints/<id>/
Purpose

Returns specific complaint details.

Update Complaint
Endpoint
PUT /api/complaints/update/<id>/
Purpose

Updates complaint information.

Delete Complaint
Endpoint
DELETE /api/complaints/delete/<id>/
Purpose

Deletes complaint.

Notifications APIs
Get Notifications
Endpoint
GET /api/notifications/
Purpose

Returns all notifications.

Create Notification
Endpoint
POST /api/notifications/create/
Purpose

Creates notification message.

Reports APIs
Complaint Reports
Endpoint
GET /api/reports/complaints/
Purpose

Returns complaint analytics.

Monthly Reports
Endpoint
GET /api/reports/monthly/
Purpose

Returns monthly complaint statistics.

Authentication Header

Protected APIs require JWT token.

Example:

Authorization: Bearer your_access_token
Docker Setup
Build Docker Image
docker build -t crm-backend .
Run Docker Container
docker run -p 8000:8000 crm-backend
AWS EC2 Deployment Steps
Connect to EC2
ssh -i your-key.pem ubuntu@your-public-ip
Clone Repository
git clone https://github.com/subhan2001/crm-backend-project.git
Install Python & venv
sudo apt update
sudo apt install python3-full python3-pip python3-venv -y
Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
Install Requirements
pip install -r requirements.txt
Run Server
python manage.py runserver 0.0.0.0:8000
Why NumPy and Pandas Used
NumPy

Used for:

Numerical calculations
Fast array processing
Analytics operations
Pandas

Used for:

Report generation
Data analysis
Complaint statistics
Monthly analytics
Future Enhancements
Kafka Integration
Jira Integration
Celery Background Tasks
Redis Caching
CI/CD Pipeline
Kubernetes Deployment
API Rate Limiting
Swagger Documentation
Author

Subhan

Python Full Stack Developer

GitHub:
https://github.com/subhan2001

License

This project is for learning and educational purposes.
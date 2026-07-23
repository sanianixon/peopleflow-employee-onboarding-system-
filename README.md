# PeopleFlow — Employee Onboarding System

PeopleFlow is a Django-based employee onboarding and document-verification application.

It provides a structured workflow for new employees to submit their personal information and required documents while allowing HR teams to review, approve or reject onboarding submissions.

## Features

### Employee Onboarding

- Create and manage an employee profile
- Store personal and employment information
- Support fresher and experienced employee types
- Track onboarding progress
- Submit onboarding details for HR review

### Document Management

- Upload required employee documents
- Configure different document types
- Mark documents as required or optional
- Track document status
- Approve or reject individual documents
- Record rejection reasons for employees

### HR Review Workflow

- View submitted employee profiles
- Review employee details and uploaded documents
- Mark applications as under review
- Approve or reject onboarding submissions
- Provide clear rejection reasons
- Track every major onboarding action

### Audit Logging

Important actions are recorded using an audit log containing:

- Employee
- Action performed
- User responsible for the action
- Date and time of the action

## Onboarding Status Flow

```text
DRAFT
  ↓
SUBMITTED
  ↓
UNDER REVIEW
  ↓
APPROVED or REJECTED
```

Employees can prepare their information in the Draft stage before formally submitting it to HR.

## Document Status Flow

```text
UPLOADED
  ↓
APPROVED or REJECTED
```

When a document is rejected, HR can provide a reason so the employee understands what must be corrected.

## Technology Stack

### Backend

- Python
- Django

### Database

- SQLite

### Frontend

- HTML
- CSS
- Django Templates

### Development Tools

- Git
- GitHub
- VS Code

## Core Models

### Employee Profile

Stores:

- Employee ID
- Employee type
- Full name
- Email address
- Phone number
- Date of birth
- Address
- Emergency contact
- Joining date
- Onboarding status
- Creation timestamp

### Document Type

Defines the documents employees may need to provide and whether each document is mandatory.

### Employee Document

Stores uploaded files, their document type, verification status, rejection reason and upload timestamp.

### Audit Log

Records important onboarding actions and the user who performed them.

## Application Workflow

1. An employee signs in to the application.
2. The employee creates or completes their profile.
3. Required documents are uploaded.
4. The employee submits the onboarding application.
5. HR reviews the employee’s details and documents.
6. HR approves or rejects individual documents.
7. The overall employee profile is approved or rejected.
8. Important actions are recorded in the audit log.

## Installation

Clone the repository:

```bash
git clone https://github.com/sanianixon/peopleflow-employee-onboarding-system-.git
```

Open the project directory:

```bash
cd peopleflow-employee-onboarding-system-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## What This Project Demonstrates

- Django model design
- One-to-one and foreign-key relationships
- Authentication-based workflows
- Role-oriented application design
- File-upload handling
- Status-driven business logic
- Document verification
- Audit logging
- Employee and HR workflow separation
- Database migrations
- Django template integration

## Future Improvements

- Email notifications for submission and approval events
- Secure cloud storage for employee documents
- File-type and file-size validation
- Malware scanning for uploaded documents
- Document expiry reminders
- More granular HR permissions
- Dashboard analytics
- Unit and integration tests
- Production deployment

## Important Note

This project is an educational prototype. A production onboarding platform would require encrypted document storage, stricter access controls, secure cloud infrastructure, file scanning and compliance with applicable data-protection requirements.

## Author

Sania Nixon

- GitHub: [sanianixon](https://github.com/sanianixon)
- LinkedIn: [Sania Nixon](https://linkedin.com/in/sania-nixon)

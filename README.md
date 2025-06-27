#  Description

This is a simple **Flask application** that allows users to post job listings and view all available job posts.  
Only authenticated users can create, update, or delete job posts.  
Users can modify or delete **only the jobs they have posted**.
## Features

- Users can register with a unique username and password.
- Users can log in using their registered credentials.
- Authenticated users can create job posts by providing relevant details.
- All users (logged in or not) can view the entire list of job posts.
- Logged-in users can update or delete only the job posts they have created.


#  Setup and Run Instructions

Follow the steps below to set up and run the Flask Job Board API on your local machine.



### 1. Install Required Packages
Make sure Python is installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
This installs all necessary dependencies such as:

Flask

Flask-SQLAlchemy

Flask-Login

mysqlclient

Werkzeug

### 2. Configure Database
Ensure MySQL is installed and running.

Then create the database and tables using the provided schema.sql file:

Via MySQL Workbench:

Open schema.sql

Execute all commands to create the user database and users/jobs tables.

Or via terminal:

bash
Copy
Edit
mysql -u root -p < schema.sql
Make sure to update app.py with your MySQL credentials:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:YourPassword@localhost/user'
For example:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Allwin%40123@localhost/user'
(Note: @ in password is encoded as %40)

### 3. Run the Flask Application
bash
Copy
Edit
python app.py
The app will run on:

cpp
Copy
Edit
http://127.0.0.1:5000/

### 4. Test with Postman
Use Postman to test the following endpoints:

Register: POST /register

Login: POST /login

Create job: POST /jobs

View jobs: GET /jobs

Update job: PUT /jobs/<id>

Delete job: DELETE /jobs/<id>

Ensure you are logged in to access protected endpoints.

# List of endpoints with sample requests
## Authentication
◉ POST /register
Register a new user.

Sample Request (JSON):

json
Copy
Edit
{
  "username": "john",
  "password": "securepass123"
}
◉ POST /login
Log in an existing user.

Sample Request:

json
Copy
Edit
{
  "username": "john",
  "password": "securepass123"
}
◉ POST /logout
Logout the current user (requires login).

◉ GET /dashboard
Access the user dashboard (requires login).

## Jobs

◉ POST /jobs
Create a new job post (requires login).

Sample Request:

json
Copy
Edit
{
  "title": "Backend Developer",
  "company_name": "TechCorp",
  "location": "Remote",
  "job_type": "Full-time",
  "description": "Build REST APIs",
  "skills": "Python, Flask, SQL",
  "reference": "TC2025"
}
◉ GET /jobs
View all jobs (with optional pagination).
Example: /jobs?page=1

◉ GET /jobs/<id>
View details of a specific job.
Example: /jobs/2

◉ PUT /jobs/<id>
Update a job (must be the job owner).
Sample Request:

json
Copy
Edit
{
  "location": "Hybrid - Bangalore"
}
◉ DELETE /jobs/<id>
Delete a job (must be the job owner).

#  Example User Credentials

Use the following credentials to test login and protected endpoints (e.g., /dashboard, /jobs):

- Username: testuser  
- Password: testpass123

(You can create this user by sending a POST request to /register with the above details.)

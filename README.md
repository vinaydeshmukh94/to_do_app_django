# Multi User Todo Application using Django

![image](https://github.com/user-attachments/assets/045823d1-d325-48d9-a6dd-83dc14edce1e)

## Description
This project is a multi-user todo application built using Django. It allows users to create, manage, and track their tasks in a collaborative environment. Whether you're working on personal tasks or team projects, this app helps you stay organized and productive.

## Features
- User registration and authentication
- Create, edit, and delete tasks
- Mark tasks as completed

## Installation
1. Clone the repository: git clone https://github.com/vinaydeshmukh94/to_do_app_django.git
2. Navigate to the project directory: cd todo
3. Install dependencies: pip install django
4. Set up the database: python manage.py makemigrationsand python manage.py migrate
5. Create a superuser for admin access: python manage.py createsuperuser
6. Start the development server: python manage.py runserver

## Usage
- Access the application through your browser at http://localhost:8000/
- Register as a new user or log in with an existing account
- Add and manage your todo tasks
- Collaborate with other users by assigning tasks to them

## Contributing
If you'd like to contribute to this project, follow these steps:
- Fork the repository
- Create a new branch: git checkout -b feature/your-feature
- Make your changes and commit them: git commit -m 'Add some feature'
- Push to the branch: git push origin feature/your-feature
- Submit a pull request

## Technologies Used
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default), can be configured for PostgreSQL or MySQL
- Authentication: Django's built-in authentication system

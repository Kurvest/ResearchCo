# JengaHub

JengaHub is an online platform that connects professionals in the construction industry with clients seeking services. Users can browse projects, send messages, and manage their profiles seamlessly.

![Alt text](static/jengaHubApp/images/buildhub2.png)


## Table of Contents

- [Features](#features)
- [Project Architecture](#project-architecture)
- [Setup Instructions](#setup-instructions)
- [Usage Guidelines](#usage-guidelines)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- Project management and display
- Messaging system between clients and professionals
- Responsive design for mobile and desktop

## Technologies Used
- **Django**: Web framework for building the application.
- **PostgreSQL**: Database for storing user and project data.
- **HTML/CSS/JavaScript**: Frontend technologies for creating user interfaces.
- **Bootstrap**: Framework for responsive design.
- **Docker**: For containerization (optional).

## Project Architecture

jengaHub/

│
├── jengaHubApp/                   # Main application

│       ├── migrations/                 # Database migrations

│   ├── templates/                  # HTML templates

│   ├── static/                     # Static files (CSS, JS, images)

│   ├── models.py                   # Database models

│   ├── views.py                    # View functions

│   ├── urls.py                     # URL routing

│   └── forms.py                    # Forms for user input
│
├── jengaHub/                       # Project settings

│   ├── __init__.py

│   ├── settings.py                 # Configuration settings

│   ├── urls.py                     # Global URL routing

│   └── wsgi.py                     # WSGI application
│
├── manage.py                       # Django command-line utility

├── requirements.txt                # Project dependencies

└── README.md                       # Project documentation

## Setup Instructions

Follow these steps to set up JengaHub on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/jengaHub.git
   cd jengaHub
   ```
2. **Create a virtual environment:**

```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies:**

```bash
Copy code
pip install -r requirements.txt
```

4. **Set up the database:**
Modify the database settings in jengaHub/settings.py according to your setup.
Run the migrations:

```bash
Copy code
python manage.py migrate
```

5. **Create a superuser for accessing the admin panel:**
   
```bash
Copy code
python manage.py createsuperuser
```

6. **Run the development server:**

```bash
Copy code
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/.

### Usage Guidelines
**Accessing the Application:**

You can view the application in your browser.
Use the login feature to authenticate as a professional or a client.

**Sending Messages:**
Navigate to the profile of a professional and use the message form to contact them.

**Managing Projects:**
Professionals can add, edit, and delete their projects through their dashboards.
- After starting the server, navigate to the home page.
- If you are an authenticated user, you can manage your profile and projects.
- Professionals can receive messages from clients and manage their projects.
- Access the admin panel at http://127.0.0.1:8000/admin/ to manage users and projects.

### Contributing
- Contributions are welcome! Please follow these steps:

1.Fork the repository.

2.Create a new branch (git checkout -b feature-branch).

3.Make your changes and commit them (git commit -m 'Add new feature').
   
6.push to the branch (git push origin feature-branch).
   
6.create a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for more details


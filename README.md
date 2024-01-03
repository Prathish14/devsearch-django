# DevSearch - Developer Search Platform 👩‍💻🔍



## Description

DevSearch is a platform that facilitates searching and connecting with developers and their projects. It enables users to discover developers, projects, exchange messages, and rate projects. As a developer, you can showcase your projects, skills, and contact information. Regular users can view developer profiles, message them, and explore projects.

### Platform:
- Web-based platform for developers and users to interact and connect.

### Components Used:
- **Frontend:**
  - HTML 🌐
  - CSS 🎨
  - JavaScript 🖥️
  - Bootstrap 🅱️

- **Backend:**
  - Python 🐍
  - Django 🌐

- **Database:** MySQL 🗃️


## Features
- Search and discover developers and their projects.
- Messaging system for communication between users and developers.
- Rating system to evaluate and vote for projects.
- Developer profile management: add projects, skills, about, and contact information.
- Secure authentication and authorization for user interactions.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    $ git clone https://github.com/Prathish14/devsearch-django.git
    $ cd DevSearch
    ```

2. **Install dependencies** from `requirements.txt`:
    ```bash
    $ pip install -r requirements.txt
    ```

3. **Configure Email for Password Reset:**
   - Open `settings.py` in your Django project.
   - Locate the email configuration section.
   - Update the following fields for Gmail SMTP:
    ```python
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = "Your_Gmail_Address"
    EMAIL_HOST_PASSWORD = "Your_Gmail_Password"
    ```

4. **Configure Database:**
   - Set up your MySQL database credentials in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'Your_Database_Name',
            'USER': 'Your_Database_User',
            'PASSWORD': 'Your_Database_Password',
            'HOST': 'Your_Database_Host',
            'PORT': 'Your_Database_Port',
        }
    }
    ```

## Usage

To run the project locally, follow these steps:

1. **Make migrations and migrate the database:**
    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

2. **Start the development server:**
    ```bash
    $ python manage.py runserver
    ```

3. **Access the application** in your browser at `http://localhost:8000/`.

## Contributing

Contributions are welcome! To contribute to DevSearch:
- Fork the repository
- Create a new branch (`git checkout -b feature`)
- Make your changes
- Commit your changes (`git commit -am 'Add feature'`)
- Push to the branch (`git push origin feature`)
- Create a new Pull Request

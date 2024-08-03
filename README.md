# CRM Django Application

This project is a simple Customer Relationship Management (CRM) application built using Django. It allows users to register, log in, view, add, update, and delete customer records. This README provides an overview of the application, setup instructions, and guidance for running the project.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Forms and Models](#forms-and-models)
7. [Running the Project](#running-the-project)
8. [Contributing](#contributing)
9. [License](#license)

## Features

- User registration and authentication
- Add, update, and delete customer records
- View individual customer records
- Basic navigation and user feedback with Bootstrap styling

## Requirements

- Python 3.x
- Django 3.x
- SQLite (default Django database)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/crmapp.git
    cd crmapp
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

- **Home:** View all customer records (requires login).
- **Add Record:** Add a new customer record.
- **Update Record:** Update an existing customer record.
- **Delete Record:** Delete a customer record.
- **Register:** Create a new user account.
- **Login:** Log in with an existing user account.
- **Logout:** Log out of the application.

## Project Structure

```
crmapp/
├── crmapp/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   ├── crmapp/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── record.html
│   │   ├── add_record.html
│   │   ├── update_record.html
│   │   ├── about.html
│   │   ├── navbar.html
├── forms.py
├── models.py
├── views.py
├── urls.py
├── manage.py
└── README.md
```

## Forms and Models

### Forms

`forms.py` contains two forms:
- `SignUpForm`: For user registration.
- `AddRecordForm`: For adding and updating customer records.

### Models

`models.py` defines a single model:
- `Record`: Represents a customer record with fields for first name, last name, email, address, city, state, and zipcode.

## Running the Project

1. **Ensure you have SQLite installed.**
   
   If you are using Gitpod, SQLite comes pre-installed. If not, refer to the SQLite installation guide for your operating system.

2. **Initialize the database with sample data:**

   You can create sample records using the Django admin interface at `http://127.0.0.1:8000/admin` after running the development server and logging in with the superuser credentials.

3. **Access and use the application:**

   - Navigate to `http://127.0.0.1:8000/` to view the homepage.
   - Register a new user or log in with an existing account to manage customer records.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

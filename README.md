# Product-management-Django-Mysql

# Product Management System

## Project Overview

The **Product Management System** is a web application built using **Django** (Python framework) and **MySQL** database. The system allows businesses and administrators to manage their product inventory efficiently through a simple interface that supports CRUD (Create, Read, Update, Delete) operations.

This system provides functionalities to:

- **Add new products** to the database.
- **View existing products** in a list format.
- **Edit product details**, including name, description, price, and stock.
- **Delete products** that are no longer needed.

It also incorporates a clean, responsive front-end built using **HTML** and **CSS** to ensure ease of use and better user experience.

### Purpose

The primary goal of this project is to provide a simple and effective platform to manage products. Whether it's for a small business or an organization, the system helps users keep track of their products, update inventory, and delete obsolete items with minimal effort.

## Features

- **Product Listing**: View all products in an organized table, with product details such as name, price, description, and stock.
- **Add Product**: Ability to add a new product by entering information like name, description, price, and available stock.
- **Edit Product**: Modify existing product details, including product name, description, price, and stock.
- **Delete Product**: Remove products from the database that are no longer needed.
- **Responsive Design**: The interface adapts to various screen sizes, making it mobile-friendly.

## Technologies Used

- **Backend**: 
  - Django (Python framework)
  - MySQL (for database management)
- **Frontend**:
  - HTML (for structuring the web pages)
  - CSS (for styling the pages)
- **Other**:
  - Python 3.x
  - Django 3.x

# 1. Create a virtual environment (optional, but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
# 3. Install the required dependencies:
  pip install -r requirements.txt
# 4. Set up MySQL database
 Log in to MySQL and create a new database:

sql
Copy code
CREATE DATABASE product_management;
Configure your MySQL database connection in settings.py (in the Django project):

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_management',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply migrations to set up the database:

bash
Copy code
python manage.py migrate

# 5. Run the server:

After completing the setup, run the Django development server:

bash
Copy code
python manage.py runserver

# 6. Access the application:

Open your web browser and go to http://127.0.0.1:8000/ to access the Product Management System.

# API Endpoints
GET /products/: Displays a list of all products.
GET /product/add/: Form to add a new product.
GET /product/edit/<int:id>/: Form to edit an existing product.
GET /product/delete/<int:id>/: Delete an existing product.
# Contributing
We welcome contributions to improve the Product Management System. If you have suggestions or improvements, feel free to open an issue or submit a pull request.

# Steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-name).
Open a pull request.
# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgements
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
MySQL: An open-source relational database management system.
HTML & CSS: For designing the front-end of the application.




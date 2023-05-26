# Django-CRM
Django CRM is a customer relationship management (CRM) system built using the Django web framework. It provides a set of features and functionalities to manage customer interactions.This readme file will guide you through the installation process and provide an overview of the system's structure and usage.

## Installation
1. Clone the repository:
``` bash
 git clone https://github.com/Husna-Hussein/Django-CRM.git
 ```
2. Change into the project directory:
``` bash
 cd Django-CRM
 ```
 3. Create a virtual environment:
 ``` bash
 python -m venv venv

 ```
 
 4. Activate the virtual environment:
    - On macOS and Linux:
    ``` bash
    source venv/bin/activate
    ```
    - On Windows:
    ``` bash 
    venv\Scripts\activate
    ```
 5. Install the dependencies:
 ``` bash 
 pip install -r requirements.txt
 ```
 6. Set up the database:
 ``` bash 
 python manage.py migrate
 ```
 7. Create a superuser account:
 ``` bash
 python manage.py createsuperuser
 ```
 8. Start the development server:
``` bash 
python manage.py runserver
```
The CRM should now be accessible at http://localhost:8000/.
## Features
Django CRM offers the following features:

- User authentication and authorization.
- Customer management: add, update, and delete customers.
## Usage
1. Access the CRM by visiting http://localhost:8000/ in your web browser.
2. Log in using your superuser account or create a new user account.
3. Explore the CRM interface and navigate through the different modules.
4. Use the navigation menu or sidebar to access various features.
5. Create, update, or delete records based on your requirements.
6. Utilize the dashboard section to gain insights into customer data.




# Fake Store API Documentation
The FakeStore API is a RESTful API for managing products, orders, carts, and more. This document provides instructions on how to clone and run the FakeStore API on your local machine.

### Prerequisites
Before you begin, make sure you have the following software installed on your computer:
  - Python 3.x
  - pip (Python package manager)
  - Virtualenv (optional but recommended for creating a virtual environment)
  - MySQL (optional)
  - Docker (optional)
  
### Clone the project 
  1. Open your terminal or command prompt.
  2. Navigate to the directory where you want to clone the FakeStore API repository.
  3. Run the following command to clone the repository:
     ```bash
        git clone "https://github.com/urs-santoshh/fake_store_api.git"
     ```

### Setup Virtual Environment (Optional)
We recommend using a virtual environment to isolate the project's dependencies. If you choose not to use a virtual environment, you can skip this step.
  1. Navigate to the project directory:
     ```bash
       cd fake_store_api
     ```
  2. Create a virtual environment (Python 3.x) and activate it:
     ```bash
       python -m venv .venv
       source venv/bin/activate  # On Windows, use "./venv/scripts/activate"
     ```
   
### Install Dependencies
  1. Install the project dependencies using pip:
     ```bash
       pip install -r requirements.txt
     ```

### Configure Environment Variables
Create a `.env` file in the project root directory and configure the following environment variables:
  ```env
    ENVIRONMENT = <your environment PRODUCTION|DEVELOPMENT>
    SECRET_KEY = <your django secret key here>
  ```

### Database Configuration Options
Choose one of the following database configuration options:

#### Option 1: MySQL in Docker Container (Recommended for this project)
If you prefer to use MySQL in a Docker container, ensure you have Docker installed on your machine. Then, follow these steps:
1. Update the .env file with your MySQL database credentials:
    ```env
      MYSQL_DATABASE = <your-database-name>
      MYSQL_HOST = <your-database-host>
      MYSQL_PASSWORD = <your-password>
      MYSQL_PORT = <Mysql default port>
      MYSQL_ROOT_PASSWORD = <your-root-password>
      MYSQL_USER = <your-username>
    ```
2. Start the MySQL container using Docker Compose:
  ```bash
      docker-compose up -d
  ```
This command launches a MySQL container configured to work with the FakeStore API.

#### Option 2: Default SQLite Database
If you prefer to use the default SQLite database included with the project, follow these steps:
1. Open the base.py file in the fakestore app settings directory.
2. Uncomment the default SQLite database settings by removing the comment (#) in front of the following lines and comment the Myswl database settings:
  ```bash
      DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

      # DATABASES = {
      #     'default': {
      #         'ENGINE': 'django.db.backends.mysql',
      #         'NAME': os.environ.get('MYSQL_DATABASE'),
      #         'USER': os.environ.get('MYSQL_USER'),
      #         'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
      #         'HOST': os.environ.get('MYSQL_HOST'),  # Use the service name defined in your Docker Compose file in production
      #         'PORT': os.environ.get('MYSQL_PORT'),   # Default MySQL port
      #     }
      # }
  ```

### Apply Migrations
Run the following commands to apply database migrations: 
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```

### Run the Development Server
Start the development server to run the FakeStore API locally:
  ```bash
      python manage.py runserver
  ```
The API should now be running at `http://127.0.0.1:8000/`.

### Create Superuser
Start the development server to run the FakeStore API locally:
  ```bash
      python manage.py createsuperuser
  ```

### Access API Documentation
You can access the API documentation by visiting the following URL in your web browser:
  ```
      http://127.0.0.1:8000/api/
  ```
This interactive documentation provides details on available API endpoints and allows you to test them.

### Usage
You can now start using the FakeStore API to manage products, orders, carts, and more. Refer to the API documentation for specific endpoints and usage instructions.

### Contributing
If you'd like to contribute to the development of the FakeStore API, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.



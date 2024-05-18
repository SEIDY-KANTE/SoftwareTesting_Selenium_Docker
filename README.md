# Django Web Application with Selenium Testing


This project is a web application developed using the Django framework and integrated with a PostgreSQL database  and testing it using Selenium. The application includes features such as login, registration, adding and listing industries, and adding and listing blog posts. The application is containerized using Docker and has been tested using the Selenium library.


## Features

- User login
- User registration
- Industry addition, listing, and detail view
- Blog post addition, listing, and detail view

## Requirements

- Docker
- Docker Compose
- Python 3.x
- PostgreSQL


## Setup and Execution

### 1. Clone the Repository

Clone the project from GitHub:
```bash
git clone https://github.com/SEIDY-KANTE/SoftwareTesting_Selenium_Docker.git
cd SoftwareTesting_Selenium_Docker
```

### 2. Running the Project with Docker

Use Docker Compose to build and start the project:
```bash
docker compose build
docker compose up -d
```

### 3. Database and Superuser Creation

The `entrypoint.sh` script handles database migrations, data loading, and creates a superuser:
```bash
#!/bin/bash

python ./manage.py makemigrations
python ./manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Seidy', 'seidy@gmail.com', '1234')" | python manage.py shell

python ./manage.py loaddata ./blogs.json
python ./manage.py loaddata ./industry.json

python ./manage.py runserver 0.0.0.0:8000
```

### 4. Running the Project

To start the project, use:
```bash
docker compose up -d
```

### 5. Running Tests

To run all tests:
```bash
python manage.py test
```

To run a specific test:
```bash
python manage.py test SoftwareTesting_Selenium_Docker.<test_name>
```
For example, to run only the blog tests:
```bash
python manage.py test SoftwareTesting_Selenium_Docker.test_blog
```

## Selenium Tests

A total of 31 UI tests have been written using the Selenium library. These tests are categorized and utilize different methods (NAME, CLASS_NAME, XPATH, CSS_SELECTOR, ID, TAG_NAME).

### Categories and Test Count

- **test_blog**: Tests for blog operations
- **test_image**: Tests for image operations
- **test_industry**: Tests for industry operations
- **test_link_filter**: Tests for link and filter operations
- **test_login_register**: Tests for user login and registration
- **test_popup**: Tests for popup operations
- **test_slider_scroll_accordion**: Tests for slider, scroll, and accordion operations
- **test_validation**: Tests for validation operations

### Methods Used and Their Counts

- `NAME`: 67 times
- `CLASS_NAME`: 48 times
- `XPATH`: 28 times
- `CSS_SELECTOR`: 35 times
- `ID`: 13 times
- `TAG_NAME`: 13 times

## Usage Instructions

1. Install Docker and Docker Compose.
2. Clone the repository and navigate to the project directory.
3. Use Docker Compose to build and start the project.
4. Run the database migrations and load the initial data.
5. Access the application at `http://localhost:8000` in your web browser.
6. Run Selenium tests to perform UI testing.


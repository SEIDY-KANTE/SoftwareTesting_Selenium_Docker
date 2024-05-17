#!/bin/bash

python ./manage.py makemigrations
python ./manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Seidy', 'seidy@gmail.com', '1234')" | python manage.py shell


python ./manage.py loaddata ./blogs.json
python ./manage.py loaddata ./industry.json


python ./manage.py runserver 0.0.0.0:8000
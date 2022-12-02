#!/bin/bash

python /code/manage.py migrate --no-input
python /code/manage.py shell < /code/init/createsuperuser.py
python /code/manage.py runserver 0.0.0.0:8000

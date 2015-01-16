#!/bin/bash

export APP_SETTINGS="project.config.DevelopmentConfig"
python manage.py create_db
python manage.py db init
python manage.py db migrate
python manage.py create_admin
python manage.py create_data

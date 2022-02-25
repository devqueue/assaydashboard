#!/bin/bash
apt-get install python3-dev default-libmysqlclient-dev build-essential
python3 -m pip install -r requirements.txt

chmod 0444 mysql.cnf

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
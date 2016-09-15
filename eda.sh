#!/bin/bash
set -e
if [ ! -d "/NCTU-EDA-Web" ]; then
    cd /
    git clone https://github.com/kevchentw/NCTU-EDA-Web
else
    cd /NCTU-EDA-Web
    git pull --rebase
fi
cd /NCTU-EDA-Web
python manage.py migrate
python manage.py runserver 0.0.0.0:8080

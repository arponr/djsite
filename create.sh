#!/bin/bash

python convert.py $1
heroku run python manage.py upload
rm upload-temp

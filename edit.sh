#!/bin/bash

python convert.py $1
git add .
git commit -a -m "edit post: $1"
git push heroku master
heroku run python manage.py upload -e

#!/bin/bash

python convert.py $1
git commit -a -m "create post: $1"
git push heroku master
heroku run python manage.py upload
rm upload-temp
git commit -a -m "delete upload-temp"
git push heroku master

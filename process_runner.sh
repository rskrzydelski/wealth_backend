#!/bin/sh

# assign port number from Dockerfile
PORT=$1

# start market-collector-service
#echo "starting alpha-vantage-service ..."
#cd market-collector-service
#python app.py &
#cd ..
#echo "done."

# start wealth-service
echo "starting django api ..."
until cd wealth-service
do
	echo "Waiting for django volume..."
done

until ./manage.py migrate
do 
	echo "Waiting for db migration to be ready..."
done

./manage.py collectstatic --noinput

gunicorn wealth.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --threads 4
echo "done."

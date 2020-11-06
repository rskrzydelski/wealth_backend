#!/bin/bash

# assign port number from Dockerfile
PORT=$1

# start alpha-vantage-service
echo "starting alpha-vantage-service ..."
cd alpha-vantage-service
python app.py &
cd ..
echo "done."

# start wealth-service
echo "starting django api ..."
cd wealth-service
gunicorn wealth.wsgi:application --bind 0.0.0.0:$PORT
cd ..
echo "done."
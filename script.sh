#!/bin/bash
echo Corriendo aplicacion...
cd /home/ubuntu/visageimage
. venv/bin/activate
sudo gunicorn --workers=5 -b 0.0.0.0:443 --certfile=cert.pem --keyfile=key.pem wsgi:application

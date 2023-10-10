#!/bin/bash 
set -euxo pipefail

python manage.py collectstatic --noinput
python manage.py migrate --noinput
release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn pacte.wsgi --log-file -

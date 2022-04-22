release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker app.asgi:application
worker: celery -A app worker -P prefork --loglevel=INFO
beat: celery -A app beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

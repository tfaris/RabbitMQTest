web: python manage.py run_gunicorn -b "0.0.0.0:$PORT"
worker: python manage.py celeryd -E -B --loglevel=INFO
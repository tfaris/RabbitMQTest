web: python Cts/manage.py run_gunicorn -b "0.0.0.0:$PORT"
worker: python Cts/manage.py celeryd -E -B --loglevel=INFO
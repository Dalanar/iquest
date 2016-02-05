release: pull collectstatic migrate

pull:
	git pull

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic

run:
	/opt/iquest/bin/python3 /opt/iquest/bin/gunicorn iquest.wsgi -b 127.0.0.1:8002
release: pull collectstatic migrate

pull:
	git pull

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic

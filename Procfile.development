web: python fastblog/manage.py runserver
worker: celery --workdir=fastblog/ --app=fastblog.celery:app worker
flower: celery --workdir=fastblog/ --app=fastblog.celery:app flower

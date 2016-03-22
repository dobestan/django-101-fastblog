clean:
	find . -name "*.pyc" -exec rm -rf {} \;


migrate:
	python fastblog/manage.py makemigrations posts users socials communications
	python fastblog/manage.py migrate


test:
	python fastblog/manage.py test posts users socials communications

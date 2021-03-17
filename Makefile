clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf bd_test
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

test:
	pipenv run pytest -s --cov=calling_plan

django-run:	
	python manage.py runserver

db-postgres:
	sudo docker run -d \
		--name bd_test \
		-e POSTGRES_PASSWORD=postgres \
    	-e PGDATA=/var/lib/postgresql/data/pgdata \
    	-v $(pwd)/bd_test:/var/lib/postgresql/data \
		-p 5432:5432 \
    	postgres:13.1

black:
	black -l79 .

shell:
	python manage.py shell_plus
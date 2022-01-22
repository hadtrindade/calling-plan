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

test:
	pytest -s --cov=calling_plan

run:	
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

db:
	docker run -d \
		--name db_dev_calling_plan \
		-e POSTGRES_PASSWORD=postgres \
    	-e PGDATA=/var/lib/postgresql/data/pgdata \
    	--mount type=volume,src=calling_plan,dst=/var/lib/postgresql/data \
		-p 5432:5432 \
    	postgres

black:
	black -l 79 calling_plan
	isort --recursive calling_plan

shell:
	python manage.py shell_plus
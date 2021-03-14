clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

test:
	pipenv run pytest -s --cov=calling_plan

django-run:
	python manage.py runserver

black:
	black -l79 .

shell:
	python manage.py shell_plus
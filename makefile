install:
	pip install -r requirements.txt
	pip install -r requirements-test.txt
	pip install -e .

test:
	pytest .

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:

format:
	black *.py
	
lint:
	flake8 *.py

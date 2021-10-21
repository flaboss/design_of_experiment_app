PYTHON_INTERPRETER = python3

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

format:
	black *.py
	
lint:
	#pylint --disable=R,C *.py
	flake8 *.py

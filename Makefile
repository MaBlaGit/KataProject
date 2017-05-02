.PHONY: test

deps:
	pip install -r requirements.txt; 
test:
	python tests/weather_api_script_tests.py
run:
	python simple_bottle_app.py


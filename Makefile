.PHONY: test

deps:
	pip install -r requirements.txt; 
test:
	python tests/weather_api_script_tests.py
run:
	python simple_bottle_app.py

docker_build:
	docker build -t Kata-Project .

USERNAME=dockermariusz
TAG= $(USERNAME)/Kata-Project

docker_push:
	@docker login --username $(USERNAME) --password $(PASSWORD) ; \
	docker tag Kata-Project $(TAG); \
	docker push $(TAG); \
	docker logout;

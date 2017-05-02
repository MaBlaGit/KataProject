.PHONY: test

deps:
	pip install -r requirements.txt; 
test:
	python tests/weather_api_script_tests.py
run:
	python simple_bottle_app.py

docker_build:
	docker build -t KataProject .

USERNAME=dockermariusz
TAG=$(USERNAME)/KataProject

docker_push:
	@docker login --username $(USERNAME) --password $(PASSWORD) ; \
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;

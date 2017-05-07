.PHONY: test

deps:
	pip install -Ur requirements.txt;
test:
	python tests/weather_api_script_tests.py
run:
	gunicorn simple_bottle_app:app

docker_build:
	docker build -t kata-project-new .

USERNAME=dockermariusz
TAG=$(USERNAME)/kata-project-new

docker_push:
	@docker login --username $(USERNAME) --password $(PASSWORD) ; \
	docker tag kata-project-new $(TAG); \
	docker push $(TAG); \
	docker logout;

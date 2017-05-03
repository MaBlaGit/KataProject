.PHONY: test

deps:
	pip install -r requirements.txt; 
test:
	python tests/weather_api_script_tests.py
run:
	python simple_bottle_app.py

docker_build:
	docker build -t kata-project .

docker_run: docker_build
	docker run \
	    --name kata-project \
	    -p 8080:8080 \
	    -d kata-project

USERNAME=dockermariusz
TAG=$(USERNAME)/kata-project

docker_push:
	@docker login --username $(USERNAME) --password $(PASSWORD) ; \
	docker tag kata-project $(TAG); \
	docker push $(TAG); \
	docker logout;

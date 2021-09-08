.PHONY: init
init:
	docker-compose build

.PHONY: run
run:
	docker-compose run --rm --service-ports app

distribute: init
	docker push test_api_app eu.gcr.io/ma-dev2/dev-images/test_api_app:latest
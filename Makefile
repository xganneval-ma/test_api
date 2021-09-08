init:
	docker-compose build

down:
	docker-compose down

run: down init
	docker-compose run -d --rm --service-ports app

distribute: init
	docker push test_api_app eu.gcr.io/ma-dev2/dev-images/test_api_app:latest
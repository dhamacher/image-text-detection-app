build-app-no-cache:
	docker build --no-cache --pull --rm -f "client\Dockerfile" -t imagetextdetectionapp:frontend-latest "client"
	docker build --no-cache --pull --rm -f "server\Dockerfile" -t imagetextdetectionapp:backend-latest "server"

build-app:
	docker build --pull --rm -f "client\Dockerfile" -t imagetextdetectionapp:frontend-latest "client"
	docker build --pull --rm -f "server\Dockerfile" -t imagetextdetectionapp:backend-latest "server"

start-app:
	docker-compose up

stop-app:
	docker-compose down

deploy-no-cache: build-app-no-cache
	docker-compose up

build-frontend:
	docker build --no-cache --pull --rm -f "client\Dockerfile" -t imagetextdetectionapp:frontend-latest "client"
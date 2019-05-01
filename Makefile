
build:
	docker build -t $(DOCKER_USER)/network-observer-flask-app_$(ARCH):$(SERVICE_VERSION) .

dev:
	docker run --publish 5000:5000 -it network-observer-flask-app /bin/sh

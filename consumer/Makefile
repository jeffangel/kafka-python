# Variables
IMAGE_NAME=consumer
DOCKERFILE_PATH=Dockerfile

# Targets
.PHONY: all build  clean

all: build

build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE_PATH) .

clean:
	docker rmi $(IMAGE_NAME)

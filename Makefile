# Directories
COMPONENTS := consumer producer
COMPOSE_FILE = docker-compose.yml

# Targets
.PHONY: all build up down clean $(COMPONENTS)

all: build up

build: $(COMPONENTS)
	@echo "All components built."

up:
	docker compose -f $(COMPOSE_FILE) up

down:
	docker compose -f $(COMPOSE_FILE) down

clean: down
	docker system prune -f
	
$(COMPONENTS):
	$(MAKE) -C $@

install: ## install server requirements
	pip install -r requirements.txt

codestyle: ## code formatting
	black --check server/app/ 
	black --check server/server/

build-docker:
	docker build -t stream4good/secureauthapi .

run-docker: build-docker
	docker run --name secureauthapi stream4good/secureauthapi
stop-docker:
	docker rm -f secureauthapi
	

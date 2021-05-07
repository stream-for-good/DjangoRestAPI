install: ## install server requirements
	pip install -r requirements.txt

codestyle: ## code formatting
	black --check server/app/ server/server/

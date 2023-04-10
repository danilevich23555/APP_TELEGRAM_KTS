
compose.up:
	docker-compose -f docker-compose.yaml up -d


run.poller:
	python3 app_Poller/Poller.py

run.worker:
	python3 app_Worcker/Worcker.py



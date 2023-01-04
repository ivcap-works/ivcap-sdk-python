
SERVICE_FILE=load_artifacts.py

run:
	PYTHONPATH=../../src python ${SERVICE_FILE} \
	  --load "$(shell date)"

run-remote:
	PYTHONPATH=../../src python ${SERVICE_FILE} \
	  --load ivcap:artifact:0000 \
		--ivcap:storage-url http://localhost:4000

run-help:
	@PYTHONPATH=../../src python ${SERVICE_FILE} -H

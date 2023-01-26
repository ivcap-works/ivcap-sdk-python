
SERVICE_FILE=img_test_service.py

GIT_COMMIT := $(shell git rev-parse --short HEAD)
GIT_TAG := $(shell git describe --abbrev=0 --tags ${TAG_COMMIT} 2>/dev/null || true)

PROJECT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

TMP_DIR=/tmp
IMG_URL=https://juststickers.in/wp-content/uploads/2016/07/go-programming-language.png

run:
	mkdir -p ${PROJECT_DIR}/data
	python ${SERVICE_FILE} \
	  --msg "$(shell date "+%d/%m-%H:%M:%S")" \
		--img-url ${IMG_URL} \
		--ivcap:out-dir ${PROJECT_DIR}/data
	@echo ">>> Output should be in '${PROJECT_DIR}/data'"

run-on-ivcap:
	rm -r ${PROJECT_DIR}/data && mkdir -p ${PROJECT_DIR}/data
	env IVCAP_INSIDE_CONTAINER=1 \
		IVCAP_ORDER_ID=8dd9006f-d1a5-4a6f-a4e2-c4b196ca14f5 \
		IVCAP_CACHE_URL=http://cache.local \
		IVCAP_STORAGE_URL=http://artifact.local \
		IVCAP_CACHE_DIR=${PROJECT_DIR}/data \
		http_proxy=http://localhost:8888 \
		https_proxy=http://localhost:8888 \
		python ${SERVICE_FILE} \
			--msg "$(shell date "+%d/%m-%H:%M:%S")" \
			--ivcap:in-dir ${PROJECT_DIR}/data \
			--ivcap:out-dir ${PROJECT_DIR}/data

run-debug:
	rm -r ${PROJECT_DIR}/data && mkdir -p ${PROJECT_DIR}/data
	env IVCAP_INSIDE_CONTAINER=1 \
		IVCAP_ORDER_ID=8dd9006f-d1a5-4a6f-a4e2-c4b196ca14f5 \
		IVCAP_CACHE_URL=http://cache.local \
		IVCAP_STORAGE_URL=http://localhost:8888 \
		IVCAP_CACHE_DIR=${PROJECT_DIR}/data \
		python ${SERVICE_FILE} \
			--msg "$(shell date "+%d/%m-%H:%M:%S")" \
			--ivcap:in-dir ${PROJECT_DIR}/data \
			--ivcap:out-dir ${PROJECT_DIR}/data
	@echo ">>> Output should be in '${PROJECT_DIR}/data'"


clean:
	rm -rf ${PROJECT_DIR}/$(shell echo ${SERVICE_FILE} | cut -d. -f1 ).dist
	rm -rf ${PROJECT_DIR}/$(shell echo ${SERVICE_FILE} | cut -d. -f1 ).build
	rm -rf ${PROJECT_DIR}/cache ${PROJECT_DIR}/data

FORCE:

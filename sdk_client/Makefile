
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
SRC_DIR:=${ROOT_DIR}/src

.PHONY: copyx

build: gen
	cd ${ROOT_DIR}
	rm -rf ${ROOT_DIR}/dist/*
	poetry build

SRC_DIR=${ROOT_DIR}/src/ivcap_client
gen:
	@if ! type "openapi-python-client" > /dev/null; then \
		echo ">>>\n>>> You need to first install 'openapi-python-client'\n>>>"; \
		exit -1; \
	fi
	rm -rf ${ROOT_DIR}/build && mkdir -p ${ROOT_DIR}/build
	cd ${ROOT_DIR}/build \
	  && curl https://raw.githubusercontent.com/reinventingscience/ivcap-core-api/main/openapi3.json -o openapi3.json \
		&& openapi-python-client generate --path openapi3.json --config ${ROOT_DIR}/config.yml \
		&& python ${ROOT_DIR}/fix_auto_generated.py \
		&& cd sdk_client/ivcap_client && mkdir client && mv *.py client \
		&& cd ${ROOT_DIR}
	rm -fr ${SRC_DIR}/api ${SRC_DIR}/models ${SRC_DIR}/client \
		&& mkdir -p ${SRC_DIR}/api ${SRC_DIR}/models ${SRC_DIR}/client \
		&& mv ${ROOT_DIR}/build/sdk_client/ivcap_client/* ${SRC_DIR} \
		&& mv ${SRC_DIR}/client/errors.py ${SRC_DIR}/client/types.py ${SRC_DIR}
	rm -r ${ROOT_DIR}/build

add-license:
	licenseheaders -t .license.tmpl -y 2023 -d src

clean:
	rm -rf *.egg-info
	rm -rf dist
	find ${ROOT_DIR} -name __pycache__ | xargs rm -r 



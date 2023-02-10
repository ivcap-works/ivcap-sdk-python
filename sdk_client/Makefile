
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

OPENAPI:=${ROOT_DIR}/../../ivap-core/api_gateway/public/openapi3.json

build: gen
	cd ${ROOT_DIR}
	poetry build

gen:
	rm -rf ${ROOT_DIR}/build && mkdir -p ${ROOT_DIR}/build
	cd ${ROOT_DIR}/build \
		&& openapi-python-client generate --path ${OPENAPI} --config ${ROOT_DIR}/config.yml \
		&& python ${ROOT_DIR}/fix_auto_generated.py \
		&& cd ${ROOT_DIR}
	rm -fr ${ROOT_DIR}/src \
		&& mkdir -p ${ROOT_DIR}/src \
		&& mv ${ROOT_DIR}/build/sdk_client/ivcap_client ${ROOT_DIR}/src
	rm -r ${ROOT_DIR}/build

add-license:
	licenseheaders -t .license.tmpl -y 2023 -d src

clean:
	rm -rf *.egg-info
	rm -rf dist
	find ${ROOT_DIR} -name __pycache__ | xargs rm -r 

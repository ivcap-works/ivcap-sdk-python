FROM python:3.9-slim-buster

# Dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends pandoc dvipng texlive-xetex texlive-latex-extra cm-super && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data/in /data/out



# Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir --user -U -r requirements.txt && \
#   rm requirements.txt && \
#   find /runner -name __pycache__ | xargs rm -rf

# Install capy


WORKDIR /sdk
RUN pip install poetry
ADD . .
RUN poetry build
#RUN pip uninstall poetry
RUN pip install dist/*.gz

ENV IVCAP_INSIDE_CONTAINER Yes

# VERSION INFORMATION
ENV IVCAP_SDK_VERSION $GIT_TAG
ENV IVCAP_SDK_COMMIT $GIT_COMMIT

WORKDIR /app
COPY examples/hello_world/hello_world.py service.py

ENTRYPOINT ["python", "/app/service.py"]

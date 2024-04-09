# Author: little-scripts

FROM python:3.11-slim-bookworm as slim-bookworm

#===========
# ARG
#===========
# ARGs need to be placed after the FROM instruction. As per https://docs.docker.com/engine/reference/builder/#arg.
# VERSION: 0.1.0.dev1 | 0.1.0a1 | 0.1.0.b1 | 0.1.0rc | 0.1.0
ARG TAG="local"
ARG VERSION="0.2.0"
ARG MAINTAINER="little-scripts <jgdevrennes@gmail.com>"

#===========
# LABEL
#===========
LABEL little-scripts.tag="${TAG}"
LABEL little-scripts.version="${VERSION}"
LABEL little-scripts.maintainer="${MAINTAINER}"
LABEL little-scripts.app="scanvulnpy"
LABEL little-scripts.src_repository="https://github.com/little-scripts/scanvulnpy"

#===========
# RUN
#===========
RUN apt-get update && \
    apt-get install -y --no-install-recommends libzip-dev zlib1g-dev libcurl4-gnutls-dev libldap2-dev zlib1g-dev libxml2-dev libfontconfig1 libpng-dev libjpeg-dev && \
    apt-get install -y && \
    apt-get clean

#===========
# WORKDIR
#===========
WORKDIR /home/little-scripts/scanvulnpy
COPY . /home/little-scripts/scanvulnpy

#===========
# INSTALL
#===========
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#===========
# ENTRYPOINT
#===========
ENTRYPOINT ["./entrypoint.sh"]

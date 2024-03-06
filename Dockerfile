# Author: little-scripts

FROM python:3.11-slim-bookworm as slim-bookworm

#===========
# ARG
#===========
# ARGs need to be placed after the FROM instruction. As per https://docs.docker.com/engine/reference/builder/#arg.
# VERSION: 0.1.0.dev1 | 0.1.0a1 | 0.1.0.b1 | 0.1.0rc | 0.1.0
ARG TAG="local"
ARG VERSION="0.1.0.dev1"
ARG BUILD_DATE="n/a"
ARG MAINTAINER="little-scripts <little-scripts@gmail.com>"

#===========
# LABEL
#===========
LABEL little-scripts.tag="${TAG}"
LABEL little-scripts.version="${VERSION}"
LABEL little-scripts.build_date="${BUILD_DATE}"
LABEL little-scripts.maintainer="${MAINTAINER}"
LABEL little-scripts.app="little-scripts"
LABEL little-scripts.src_repository="https://github.com/little-scripts/little-scripts-images"

#===========
# RUN
#===========
RUN apt-get update && \
    apt-get install -y --no-install-recommends libzip-dev zlib1g-dev libcurl4-gnutls-dev libldap2-dev zlib1g-dev libxml2-dev libfontconfig1 libpng-dev libjpeg-dev && \
    apt-get install -y && \
    apt-get clean

#===========
# WORKDIR/COPY/INSTALL
#===========
WORKDIR /home/little-scripts/scanvulnpy
COPY . /home/little-scripts/scanvulnpy
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#===========
# ENTRYPOINT
#===========
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD ["python -m scanvulnpy -r ./requirements.txt"]

FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip \
	python3-venv ocl-icd-libopencl1 clinfo\
&& rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ARG XSUITE_VERSION=latest

RUN python3 -m pip install --upgrade pip &&\
	python3 -m pip install --no-cache-dir xsuite==${XSUITE_VERSION} pyopencl

CMD ["bash"]
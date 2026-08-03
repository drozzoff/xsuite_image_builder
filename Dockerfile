FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip python3-venv \
&& rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ARG XSUITE_VERSION=latest

RUN python3 -m pip install --upgrade pip &&\
	python3 -m pip install --no-cache-dir xsuite==${XSUITE_VERSION}

ARG TOOLBOX_REF=9a2eac0eb29d28d3b45883dec4bc5251e6b6442a

RUN /opt/venv/bin/python -m pip install --no-cache-dir "https://github.com/drozzoff/toolbox/archive/${TOOLBOX_REF}.zip" \
&& /opt/venv/bin/python -c "import toolbox; print(toolbox.__file__)"
	
CMD ["bash"]
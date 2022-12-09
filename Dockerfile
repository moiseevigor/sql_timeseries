FROM ubuntu

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        libx11-6 \
        ca-certificates \
        python3 \
        python3-setuptools \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
FROM ubuntu

RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
    postgresql-client \
    python3-pip && \
#    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
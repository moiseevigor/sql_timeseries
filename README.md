# SQL Time series
Experimentation of Time series in PostgreSQL.

## Build & Run

<!-- Build

```
docker build -t sql_timeseries -f Dockerfile .
```

run container

```
xhost local:root
docker run --rm -it -v $PWD:/app sql_timeseries python /app/run.py
``` -->

Run with docker-compose, should bring up PostgreSQL service on port 5432/tcp

```
docker-compose up
```

Check if everything works fine 

```
docker-compose ps
       Name                      Command              State           Ports         
------------------------------------------------------------------------------------
sql_timeseries_db_1   docker-entrypoint.sh postgres   Up      0.0.0.0:5432->5432/tcp
```

Init DB

```
$ bash rundb.sh postgres postgres initdb
Password for user postgres:
NOTICE:  database "timeseries" does not exist, skipping
DROP DATABASE
CREATE DATABASE
CREATE ROLE
GRANT
```

Create schema 

```
$ bash rundb.sh tsuser timeseries schema
Password for user tsuser: 
NOTICE:  table "log_1" does not exist, skipping
DROP TABLE
CREATE TABLE
ALTER TABLE
NOTICE:  index "idx_created_at" does not exist, skipping
DROP INDEX
CREATE INDEX
```

Run tests

```
docker-compose up app
```

## Problem statement 

Time series data are quite common in many applications. Some of them are logging, time series events from sensors in IoT, time series data on stock market etc.

Assumptions:

1. Table accepting inserts at regular intervals with some minor jitter
2. Zero or no updates are effected on inserted records
3. 

## Results

- Measure index performance with number of records growth, compute time on random range search 
- Random vs regular timestamps 


### Experiment 1: Sequential run 
Insert was emitted as separate statement, not batching

```
# app_1  | The create array 500K elements: 7.245429991999117
# app_1  | The insert of 500K elements: 504.2107125670009
```

Sizes

```
log_1: "63 MB"
idx_created_at: "19 MB"
```

Approx inserting at 1K records per sec.

### Experiment 2: Sequential run disable index

See https://fle.github.io/temporarily-disable-all-indexes-of-a-postgresql-table.html


### Experiment 3: Batching

### Experiment 4: Types of indexes on datetime 
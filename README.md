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

## Results

### Sequential run 
Insert was emitted as separate statement, not batching

```
# app_1  | The create array 500K elements: 7.245429991999117
# app_1  | The insert of 500K elements: 504.2107125670009
```

Approx inserting at 1K records per sec.


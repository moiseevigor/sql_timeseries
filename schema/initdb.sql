DROP DATABASE IF EXISTS timeseries;
-- REASSIGN OWNED BY tsuser TO postgres;  -- or some other trusted role
-- DROP OWNED BY tsuser;
DROP USER IF EXISTS tsuser;

CREATE DATABASE timeseries;
CREATE USER tsuser WITH ENCRYPTED PASSWORD 'example';
GRANT ALL PRIVILEGES ON DATABASE timeseries TO tsuser;


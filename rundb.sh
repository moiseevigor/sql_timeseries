#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --host localhost --username "$1" --dbname "$2" < ./schema/$3.sql
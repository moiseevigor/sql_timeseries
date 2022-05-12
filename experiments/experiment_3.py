###########################################################################
## Experiment 3: Progressively insert records in table log_1 and measure 
##   range query speed drop and plot the graph. We'd like to establish the
##   baseline of index performance. Types of indexes are BTREE and BRIN

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import text
import random
import numpy as np

from datetime import datetime, timedelta
from pytz import timezone
import timeit
UTC = timezone('UTC')

def run():
    engine = create_engine('postgresql://tsuser:example@db:5432/timeseries')

    with engine.connect() as con: 
        benchmarks = {
            'values': [],
            'errors': []
        }

        log_types = []
        len_log_types = 200
        res_log_types = con.execute("select * from log_types");
        
        for res in res_log_types:
            log_types.append(res);

        if len(log_types) == 0:
            timebench = timeit.default_timer()
            for i in range(0, len_log_types):
                log_types.append({ 
                    "uuid": uuid.uuid1(), 
                    "created_at": datetime(2021, 5, 11, 16, 00, 00, 000000, tzinfo=UTC), 
                    "text": i 
                })
            print(f"Create array {len_log_types} elements:", timeit.default_timer() - timebench)
            statement = text("""INSERT INTO log_types(uuid, created_at, text) VALUES (:uuid, :created_at, :text)""")
            con.execute(statement, log_types)

        # LOOP 1: main loop 
        len_logs = 10000
        num_experiments = 500
        for m in range(0, num_experiments):

            # LOOP 2: insert progressively batch of records 
            # timebench = timeit.default_timer()
            data = []
            for i in range(0, len_logs):
                created_at = datetime(2022, 5, 11, 17, 00, 00, 000000, tzinfo=UTC) \
                        + timedelta(seconds=m*len_logs + i*1/6+random.random())
                data.append({ 
                    "uuid": uuid.uuid1(), 
                    "type_uuid": log_types[int(random.random()*len_log_types)]['uuid'], 
                    "created_at": created_at,
                    "text": i 
                })
            # print(f"The create array {len_logs} elements: ", timeit.default_timer() - timebench)
            
            timebench = timeit.default_timer()

            statement = text("""INSERT INTO log_1(uuid, type_uuid, created_at, text) VALUES (:uuid, :type_uuid, :created_at, :text)""")
            con.execute(statement, data)

            print(f"Experiment 3: The batch insert of {len_logs} elements on iteration {m}: ", timeit.default_timer() - timebench)

            # LOOP 3: run range queries
            run_benchmarks = []
            for n in range(0, 100):
                # random_hour = random.randint(1,24) + random.random()
                random_hour = 24
                timebench = timeit.default_timer()

                res_log_types = con.execute(
                    "SELECT DISTINCT ON (type_uuid) * FROM public.log_1 " + \
                    "INNER JOIN log_types on log_1.type_uuid = log_types.uuid " + \
                    "WHERE " + \
                   f"     log_1.created_at < CURRENT_TIMESTAMP + '{random_hour + random.random()} HOURS'::interval " + \
                   f"AND log_1.created_at > CURRENT_TIMESTAMP - '{random_hour + random.random()} HOURS'::interval " + \
                    "ORDER BY type_uuid, log_1.created_at desc");

                res_log_types.fetchall()
                benchtime_ms = round((timeit.default_timer() - timebench)*1000)
                run_benchmarks.append(benchtime_ms)
                print(f"Experiment 3: Select speed on iter. {m},\t rowcount {res_log_types.rowcount},\t {random_hour} HOURS,\t num records in table {len_logs*m}:\t", benchtime_ms, "ms")
            
            print(f"Experiment 3: Benchmarks Mean: ", np.array(run_benchmarks).mean(), "\t Std. error:", np.array(run_benchmarks).std())
            benchmarks['values'].append(np.array(run_benchmarks).mean())
            benchmarks['errors'].append(np.array(run_benchmarks).std())
            
        print("Benchmarks: ", benchmarks)




###########################################################################
## Experiment 2: The batch insert of 500K elements: 175.64663429999928 sec

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import text
import random

from datetime import datetime, timedelta
from pytz import timezone
import timeit
UTC = timezone('UTC')

def run():
    engine = create_engine('postgresql://tsuser:example@db:5432/timeseries')

    with engine.connect() as con: 
        log_types = []
        len_log_types = 200
        res_log_types = con.execute("select * from log_types");
        for res in res_log_types:
            log_types.append(res);

        # timebench = timeit.default_timer()
        # log_types = []
        # for i in range(0, len_log_types):
        #     log_types.append({ 
        #         "uuid": uuid.uuid1(), 
        #         "created_at": datetime(2021, 5, 11, 16, 00, 00, 000000, tzinfo=UTC), 
        #         "text": i 
        #     })
        # print(f"The create array {len_log_types} elements:", timeit.default_timer() - timebench)
        # statement = text("""INSERT INTO log_types(uuid, created_at, text) VALUES (:uuid, :created_at, :text)""")
        # con.execute(statement, log_types)

        timebench = timeit.default_timer()
        len_logs = 500000
        data = []
        for i in range(0, len_logs):
            data.append({ 
                "uuid": uuid.uuid1(), 
                "type_uuid": log_types[int(random.random()*len_log_types)]['uuid'], 
                "created_at": datetime(2022, 5, 11, 17, 00, 00, 000000, tzinfo=UTC) + timedelta(seconds=i*1/6+random.random()), 
                "text": i 
            })
        print(f"The create array {len_logs} elements:", timeit.default_timer() - timebench)

        timebench = timeit.default_timer()
        
        statement = text("""INSERT INTO log_1(uuid, type_uuid, created_at, text) VALUES (:uuid, :type_uuid, :created_at, :text)""")
        con.execute(statement, data)

        print(f"Experiment 2: The batch insert of 500K elements:", timeit.default_timer() - timebench)

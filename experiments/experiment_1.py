###########################################################################
## Experiment 1

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
        timebench = timeit.default_timer()
        data = []
        for i in range(0, 500000):
            data.append({ 
                "uuid": uuid.uuid1(), 
                "created_at": datetime(2022, 4, 1, 20, 38, 28, 964690, tzinfo=UTC) + timedelta(seconds=i*60), 
                "text": i 
            })
        print(f"The create array 500K elements:", timeit.default_timer() - timebench)

        timebench = timeit.default_timer()
        statement = text("""INSERT INTO log_1(uuid, created_at, text) VALUES (:uuid, :created_at, :text)""")
        for line in data:
            con.execute(statement, **line)

        print(f"The insert of 500K elements:", timeit.default_timer() - timebench)

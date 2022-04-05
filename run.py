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

engine = create_engine('postgresql://tsuser:example@db:5432/timeseries')

metadata = MetaData()
logs = Table('log_1', metadata,
    Column('uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('type_uuid', UUID(as_uuid=True), default=uuid.uuid4),
    Column('created_at', DateTime),
    Column('text', String),
)
# metadata.create_all(engine)

# datetime.datetime(2022, 4, 2, 20, 38, 28, 964690, tzinfo=<UTC>)
# datetime.now(UTC)

###########################################################################
## Experiment 1
# with engine.connect() as con:
#     log_types = []
#     res_log_types = con.execute("select * from log_types");
#     for res in res_log_types:
#         log_types.append(res);
#
#     timebench = timeit.default_timer()
#     data = []
#     for i in range(0, 500000):
#         data.append({ 
#             "uuid": uuid.uuid1(), 
#             "type_uuid": uuid.uuid1(), 
#             "created_at": datetime(2022, 4, 1, 20, 38, 28, 964690, tzinfo=UTC) + timedelta(seconds=i*60), 
#             "text": i 
#         })
#     print(f"The create array 500K elements:", timeit.default_timer() - timebench)

#     timebench = timeit.default_timer()
#     statement = text("""INSERT INTO log_1(uuid, type_uuid, created_at, text) VALUES (:uuid, :type_uuid, :created_at, :text)""")
#     for line in data:
#         con.execute(statement, **line)

#     print(f"Experiment 1: The sequential insert of 500K elements:", timeit.default_timer() - timebench)


###########################################################################
## Experiment 2: The batch insert of 500K elements: 175.64663429999928 sec
with engine.connect() as con: 
    # log_types = []
    # res_log_types = con.execute("select * from log_types");
    # for res in res_log_types:
    #     log_types.append(res);

    timebench = timeit.default_timer()
    len_log_types = 200
    log_types = []
    for i in range(0, len_log_types):
        log_types.append({ 
            "uuid": uuid.uuid1(), 
            "created_at": datetime(2022, 4, 1, 20, 38, 28, 964690, tzinfo=UTC), 
            "text": i 
        })
    print(f"The create array 200 elements:", timeit.default_timer() - timebench)
    statement = text("""INSERT INTO log_types(uuid, created_at, text) VALUES (:uuid, :created_at, :text)""")
    con.execute(statement, log_types)


    timebench = timeit.default_timer()
    len_logs = 500000
    data = []
    for i in range(0, len_logs):
        data.append({ 
            "uuid": uuid.uuid1(), 
            "type_uuid": log_types[int(random.random()*len_log_types)]['uuid'], 
            "created_at": datetime(2022, 4, 1, 20, 38, 28, 964690, tzinfo=UTC) + timedelta(seconds=i*1/6+random.random()), 
            "text": i 
        })
    print(f"The create array 500K elements:", timeit.default_timer() - timebench)

    timebench = timeit.default_timer()
    
    statement = text("""INSERT INTO log_1(uuid, type_uuid, created_at, text) VALUES (:uuid, :type_uuid, :created_at, :text)""")
    con.execute(statement, data)

    print(f"Experiment 2: The batch insert of 500K elements:", timeit.default_timer() - timebench)


###########################################################################
# with engine.connect() as con:
#     rs = con.execute("SELECT * FROM public.log_1 WHERE created_at < CURRENT_TIMESTAMP - '2 MINUTES'::interval")

#     for row in rs:
#         print(row)

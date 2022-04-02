import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import text

from datetime import datetime
from pytz import timezone
UTC = timezone('UTC')

engine = create_engine('postgresql://tsuser:example@db:5432/timeseries')

# metadata = MetaData()
# books = Table('log_1', metadata,
#     # Column('id', Integer, primary_key=True),
#     Column('uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
#     Column('created_at', DateTime),
#     Column('text', String),
# )
# metadata.create_all(engine)

# datetime.datetime(2022, 4, 2, 20, 38, 28, 964690, tzinfo=<UTC>)

with engine.connect() as con:
    data = ( 
        { "uuid": uuid.uuid1(), "created_at": datetime.now(UTC), "text": "11111" },
        { "uuid": uuid.uuid1(), "created_at": datetime.now(UTC), "text": "22222" },
    )

    statement = text("""INSERT INTO log_1(uuid, created_at, text) VALUES(:uuid, :created_at, :text)""")

    for line in data:
        con.execute(statement, **line)

with engine.connect() as con:
    rs = con.execute('SELECT * FROM log_1')

    for row in rs:
        print(row)

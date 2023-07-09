import sqlalchemy, os
from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)

db_connection_string = os.environ['db_connection_string']


engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
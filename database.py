import sqlalchemy, os
from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)

db_connection_string = os.environ['db_connection_string']


engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})
    
def load_jobs_from_db():
  with engine.connect() as conn:  # Use with loop so db closes when loop ends
    result = conn.execute(text("select * from jobs"))
    
    result_dicts = []
    for row in result.all():
      result_dicts.append(dict(row._mapping))
    return result_dicts
  #allresults = result.all() # A list of rows from the query results
  #firstresult = allresults[0]
  #firstresult_dict = dict(allresults[0]._mapping) # Row to Dict needs mapping of column names


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs where id = {id}")) #Python string+var format
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)
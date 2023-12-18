from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connection_string = "mysql+mysqlconnector://user1:pscale_pw_abc123@us-east.connect.psdb.cloud:3306/sqlalchemy"
connection_string = "mysql+mysqlconnector://root:root@localhost:8889/ibarber"
engine = create_engine(connection_string, echo=True)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connection_string = "mysql+mysqlconnector://root:root@localhost:8889/ibarber"
connection_string = "mysql+mysqlconnector://root:lUfFqfNObKIcGEcLtZSIkhkObffnCOnd@hopper.proxy.rlwy.net:56850/ibarber"
engine = create_engine(connection_string, echo=True)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()


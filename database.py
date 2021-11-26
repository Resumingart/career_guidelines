import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class career(Base):

    __tablename__ = "careers"
    id =Column(Integer, primary_key=True)
    name = Column(String)
    college = Column(String)
    stream = Column(String)
    email = Column(String)

class login(Base):
    __tablename__ = "logins"
    id = Column(Integer,primary_key=True)
    email = Column(String)
    password = Column(String)


if __name__ == "__main__":
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
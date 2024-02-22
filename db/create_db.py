from sqlalchemy import create_engine
engine = create_engine('sqlite:///Project1/db/.db')
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float
class roll_call(Base):
    __tablename__='ID'
    Index = Column(Integer,primary_key=True,autoincrement=True)
    ID = Column(String)

    def __str__(self)->str:
        return self.ID
Base.metadata.create_all(engine)





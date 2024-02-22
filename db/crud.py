from sqlalchemy.orm import sessionmaker
from Project1.db.create_db import engine, roll_call
Ojsession=sessionmaker(engine)
ojsession=Ojsession()
def check_in(identification: int):
    employee = roll_call(ID=identification)
    ojsession.add(employee)
    ojsession.commit()
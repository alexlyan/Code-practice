from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///server_db.db', echo=True)

Base = declarative_base()

class TwitTable(Base):
    __tablename__ = 'twitter_table'

    # twit columns

    Id = Column(Integer, primary_key=True)
    Time_stamp = Column(Integer)
    Username = Column(String)
    Text = Column(String)
    Hashtags = Column(String)
    User_mentions = Column(String)
    Location = Column(String)

    def __repr__(self):
        return f"<twitter_table(" \
                f"Id = {self.Id}," \
                f"Username = {self.Username}," \
                f"Time_stamp = {self.Time_stamp}, " \
                f"Text = {self.Text}," \
                f"Hashtags = {self.Hashtags}," \
                f"User_mentions = {self.User_mentions}," \
                f"Location = {self.Location})>"

def db_init():
    Base.metadata.create_all(engine)
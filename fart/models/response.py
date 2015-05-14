from sqlalchemy import Column, Integer, String, Date, Binary
from fart.models import Base


class Response(Base):
    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True)
    httpversion = Column(String)
    headers = Column(String)
    content = Column(Binary)
    timestamp_start = Column(Date)
    timestamp_end = Column(Date)

    def __init__(self, httpversion, headers, content, timestamp_start,
                 timestamp_end):
        self.httpversion = httpversion
        self.headers = headers
        self.content = content
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end

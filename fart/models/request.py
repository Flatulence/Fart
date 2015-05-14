from sqlalchemy import Column, Integer, String, Date, Binary
from fart.models import Base


class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    method = Column(String)
    host = Column(String)
    port = Column(String)
    path = Column(String)
    httpversion = Column(String)
    headers = Column(String)
    content = Column(Binary)
    timestamp_start = Column(Date)
    timestamp_end = Column(Date)

    def __init__(self, method, host, port, path, httpversion, headers, content,
                 timestamp_start, timestamp_end):
        self.method = method
        self.host = host
        self.port = port
        self.path = path
        self.httpversion = httpversion
        self.headers = headers
        self.content = content
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end

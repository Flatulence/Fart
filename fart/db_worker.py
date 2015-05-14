from fart.models.request import Request
from fart.models.response import Response


def init_worker(q, Session):
    session = Session()
    while True:
        httpTransaction = q.get()
        req = httpTransaction["request"]
        res = httpTransaction["response"]

        print type(req.timestamp_start)
        incomingReq = Request(req.method, req.host, req.port, req.path,
                              req.httpversion, req.headers, req.content,
                              req.timestamp_start, req.timestamp_end)

        incomingRes = Response(res.httpversion, res.headers, res.content,
                               res.timestamp_start, res.timestamp_end)

        session.add(incomingReq)
        session.add(incomingRes)

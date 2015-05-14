from datetime import datetime
from fart.models.request import Request
from fart.models.response import Response


def init_worker(q, Session):
    session = Session()
    while True:
        httpTransaction = q.get()
        req = httpTransaction["request"]
        res = httpTransaction["response"]

        req_timestamp_start = datetime.utcfromtimestamp(req.timestamp_start)
        req_timestamp_end = datetime.utcfromtimestamp(req.timestamp_end)
        req_httpversion = '{0}.{1}'.format(str(req.httpversion[0]),
                                           str(req.httpversion[1]))
        req_headers = str(req.headers)

        incomingReq = Request(req.method, req.host, req.port, req.path,
                              req_httpversion, req_headers, req.content,
                              req_timestamp_start, req_timestamp_end)

        res_httpversion = '{0}.{1}'.format(str(req.httpversion[0]),
                                           str(req.httpversion[1]))
        res_headers = str(res.headers)
        res_timestamp_start = datetime.utcfromtimestamp(res.timestamp_start)
        res_timestamp_end = datetime.utcfromtimestamp(res.timestamp_end)

        incomingRes = Response(res_httpversion, res_headers, res.content,
                               res_timestamp_start, res_timestamp_end)

        session.add(incomingReq)
        session.add(incomingRes)

        session.commit()

        for request in session.query(Request).order_by(Request.id):
            print request.path

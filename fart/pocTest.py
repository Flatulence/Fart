#!/usr/bin/env python
"""
This example builds on mitmproxy's base proxying infrastructure to
implement functionality similar to the "sticky cookies" option.

Heads Up: In the majority of cases, you want to use inline scripts.
"""
from libmproxy import controller, proxy
from libmproxy.proxy.server import ProxyServer
from libmproxy.protocol.http import HTTPResponse
from netlib.odict import ODictCaseless


class StickyMaster(controller.Master):
    def __init__(self, server, q):
        controller.Master.__init__(self, server)
        self.stickyhosts = {}
        self.q = q

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, flow):
        print 'Got request'
        if flow.request.pretty_host(hostheader=True).endswith(".fart"):
            resp = HTTPResponse(
                [1, 1], 200, "OK",
                ODictCaseless([["Content-Type", "text/html"]]),
                "PFFTTTTTTTTT")
            flow.reply(resp)
        else:
            flow.reply()

    def handle_response(self, flow):
        hid = (flow.request.host, flow.request.port)
        if flow.response.headers["set-cookie"]:
            self.stickyhosts[hid] = flow.response.headers["set-cookie"]
        flow.reply()


def init_proxy(q):
    print 'kicking shit off fucking um I would print the interface that the'
    config = proxy.ProxyConfig(port=8080)
    server = ProxyServer(config)
    m = StickyMaster(server, q)
    m.run()

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
        if flow.request.pretty_host(hostheader=True).endswith(".fart"):
            resp = HTTPResponse(
                [1, 1], 301, "Redirect",
                ODictCaseless([["Content-Type", "text/html"]]),
                '<meta http-equiv="refresh" content="0; url=http://localhost:6543" />')
            flow.reply(resp)
        else:
            flow.reply()

    def handle_response(self, flow):
        httpTransaction = {}
        httpTransaction["request"] = flow.request
        httpTransaction["response"] = flow.response
        self.q.put(httpTransaction)
        flow.reply()


def init_proxy(q,fartconfig):
    settings = fartconfig.registry.settings
    port = settings['proxy_port']
    config = proxy.ProxyConfig(port=int(port))
    server = ProxyServer(config)
    m = StickyMaster(server, q)
    m.run()

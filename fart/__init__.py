"""Main entry point
"""
from pyramid.config import Configurator
from libmproxy import controller, proxy
from libmproxy.proxy.server import ProxyServer

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("fart.views")
    return config.make_wsgi_app()

config = proxy.ProxyConfig(port=8080)
server = ProxyServer(config)
m = StickyMaster(server)
m.run()

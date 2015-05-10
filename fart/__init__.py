"""Main entry point
"""
from threading import Thread
from Queue import Queue
from .pocTest import init_proxy
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("fart.views")

    q = Queue()
    t = Thread(target=init_proxy, args=(q,))
    t.start()

    return config.make_wsgi_app()

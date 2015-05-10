"""Main entry point
"""
from threading import Thread
from Queue import Queue
from fart.proxy import init_proxy
from pyramid.config import Configurator
from fart.models import initialize_sql
from fart.db_worker import init_worker

def main(global_config, **settings):
    Session = initialize_sql()
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("fart.views")

    q = Queue()
    proxy_thread = Thread(target=init_proxy, args=(q,))
    db_thread = Thread(target=init_worker, args=(q,Session,))
    proxy_thread.start()
    db_thread.start()

    return config.make_wsgi_app()

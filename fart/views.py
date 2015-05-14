""" Cornice services.
"""
from cornice import Service


hello = Service(name='hello', path='/', description="Simplest app")
get_history = Service(name='get_history', path='/api/get_history')

@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

@get_history.get()
def get_history(request):
    params = request.GET()
    if page in params:
        try:
            page = int(params["page"])
            return ["httpTransaction1", "httpTransaction2"]
        except ValueError:
            pass
    return "invalid request!"



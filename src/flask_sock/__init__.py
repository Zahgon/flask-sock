from functools import wraps
from flask import Blueprint, request, Response, current_app
from simple_websocket import Server, ConnectionClosed


class Sock:
    """Instantiate the Flask-Sock extension.

    :param app: The Flask application instance. If not provided, it must be
                initialized later by calling the :func:`Sock.init_app` method.
    """
    def __init__(self, app=None):
        self.app = None
        self.bp = None
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        """Initialize the Flask-Socket extension.


        :param app: The Flask application instance. This method only needs to
                    be called if the application instance was not passed as
                    an argument to the constructor.
        """
        pass

    def route(self, path, bp=None, **kwargs):
        """Decorator to create a WebSocket route.

        The decorated function will be invoked when a WebSocket client
        establishes a connection, with a WebSocket connection object passed
        as an argument. Example::

            @sock.route('/ws')
            def websocket_route(ws):
                # The ws object has the following methods:
                # - ws.send(data)
                # - ws.receive(timeout=None)
                # - ws.close(reason=None, message=None)

        If the route has variable components, the ``ws`` argument needs to be
        included before them.

        :param path: the URL associated with the route.
        :param bp: the blueprint on which to register the route. If not given,
                   the route is attached directly to the Flask application
                   instance. When a blueprint is used, the application is
                   responsible for the blueprint's registration.
        :param kwargs: additional route options. See the Flask documentation
                       for the ``app.route`` decorator for details.
        """
        pass

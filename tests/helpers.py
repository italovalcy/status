"""Module with utilities to create tests."""
from unittest.mock import Mock

from kytos.core import Controller
from kytos.core.config import KytosConfig


def get_controller_mock():
    """Return a controller mock."""
    options = KytosConfig().options['daemon']
    controller = Controller(options)
    controller.log = Mock()
    return controller


def get_test_client(controller, napp):
    """Return a flask api test client."""
    controller.api_server.register_napp_endpoints(napp)
    return controller.api_server.app.test_client()

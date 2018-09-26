"""Module to test the main napp file."""
from unittest import TestCase
from unittest.mock import Mock

from kytos.core import Controller
from kytos.core.config import KytosConfig

from napps.kytos.status.main import Main


class TestMain(TestCase):
    """Test the Main class."""

    def setUp(self):
        """Execute steps before each tests.

        Set the server_name_url_url from kytos/mef_eline
        """
        self.server_name_url = 'http://localhost:8181/api/kytos/mef_eline'
        self.napp = Main(self.get_controller_mock())

    def test_get_event_listeners(self):
        """Verify all event listeners registered."""
        expected_events = ['kytos/core.shutdown',
                           'kytos/core.shutdown.kytos/status']
        actual_events = self.napp.listeners()
        self.assertEqual(expected_events, actual_events)

    def test_verify_api_urls(self):
        """Verify all APIs registered."""
        expected_urls = [
            ({}, {'OPTIONS', 'HEAD', 'GET'}, '/api/kytos/status/v1/napps'),
            ({}, {'OPTIONS', 'GET', 'HEAD'}, '/api/kytos/status/v1/')]
        urls = self.get_napp_urls(self.napp)
        self.assertEqual(expected_urls, urls)

    @staticmethod
    def get_controller_mock():
        """Return a controller mock."""
        options = KytosConfig().options['daemon']
        controller = Controller(options)
        controller.log = Mock()
        return controller

    @staticmethod
    def get_napp_urls(napp):
        """Return the kytos/mef_eline urls.

        The urls will be like:

        urls = [
            (options, methods, url)
        ]

        """
        controller = napp.controller
        controller.api_server.register_napp_endpoints(napp)

        urls = []
        for rule in controller.api_server.app.url_map.iter_rules():
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            if f'{napp.username}/{napp.name}' in str(rule):
                urls.append((options, rule.methods, f'{str(rule)}'))

        return urls

    @staticmethod
    def get_app_test_client(napp):
        """Return a flask api test client."""
        napp.controller.api_server.register_napp_endpoints(napp)
        return napp.controller.api_server.app.test_client()

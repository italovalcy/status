"""Test Main methods."""
from unittest import TestCase
from unittest.mock import MagicMock, patch

from kytos.lib.helpers import get_controller_mock, get_test_client


class TestMain(TestCase):
    """Test the Main class."""

    API_URL = "http://127.0.0.1:8181/api/kytos/status"

    def setUp(self):
        """Execute steps before each tests."""
        patch('kytos.core.helpers.run_on_thread', lambda x: x).start()
        from napps.kytos.status.main import Main
        self.addCleanup(patch.stopall)

        self.napp = Main(get_controller_mock())

    @patch('kytos.core.Controller.status', return_value='status')
    def test_get_controller_status(self, _):
        """Test get_controller_status method."""
        api = get_test_client(self.napp.controller, self.napp)
        url = "%s/v1/" % self.API_URL
        response = api.open(url, method='GET')

        self.assertEqual(response.json, {'status': 'status'})
        self.assertEqual(response.status_code, 200)

    def test_get_napps_info(self):
        """Test get_napps_info method."""
        napps = []
        for index in range(0, 2):
            napp = MagicMock()
            napp.author = 'author'
            napp.name = 'name'
            napp.version = 'version'
            napp.description = 'description'
            napp.license = 'license'
            napp.tags = 'tags'
            napps.append(napp)
            self.napp.controller.napps.update({index: napp})

        api = get_test_client(self.napp.controller, self.napp)
        url = "%s/v1/napps" % self.API_URL
        response = api.open(url, method='GET')

        response_napps = response.json['napps']
        for index, napp in enumerate(napps):
            response_napp = response_napps[index]
            self.assertEqual(response_napp['name'], 'author/name')
            self.assertEqual(response_napp['version'], 'version')
            self.assertEqual(response_napp['description'], 'description')
            self.assertEqual(response_napp['license'], 'license')
            self.assertEqual(response_napp['tags'], 'tags')
        self.assertEqual(response.status_code, 200)

"""Main module of kytos/status Kytos Network Application.

Provides basic information about the controller status
"""

from kytos.core import KytosNApp, log, rest

from napps.kytos.status import settings
from flask import jsonify

import json

class Main(KytosNApp):
    """Main class of kytos/status NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        pass

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        pass

    @rest('v1/')
    def get_controller_status(self):
        """Return basic information from running controller."""
        status = self.controller.status()
        return jsonify({'status': status})

    @rest('v1/napps')
    def get_napps_info(self):
        """Return a list of all NApps installed and running."""
        napps = [ napp[1] for napp in self.controller.napps.items() ]
        output = []
        for napp in napps:
            output.append({'name': "{}/{}".format(napp.author, napp.name),
                           'version': napp.version,
                           'description': napp.description,
                           'license': napp.license,
                           'tags': napp.tags})
        return jsonify({'napps': output})

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass

"""Main module of kytos/status Kytos Network Application."""
from flask import jsonify

from kytos.core import KytosNApp, rest


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

    def execute(self):
        """Procedures executed after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """

    @rest('v1/')
    def get_controller_status(self):
        """Return basic information from running controller."""
        status = self.controller.status()
        return jsonify({'status': status})

    @rest('v1/napps')
    def get_napps_info(self):
        """Return a list of all NApps installed and running."""
        napps = [napp[1] for napp in self.controller.napps.items()]
        output = []
        for napp in napps:
            output.append({'name': "{}/{}".format(napp.author, napp.name),
                           'version': napp.version,
                           'description': napp.description,
                           'license': napp.license,
                           'tags': napp.tags})
        return jsonify({'napps': output})

    def shutdown(self):
        """Shutdown the napp when the napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """

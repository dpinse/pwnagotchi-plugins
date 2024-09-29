import pwnagotchi.plugins as plugins

class MacAddressLogger(plugins.Plugin):
    __author__ = 'Deus Dust'
    __version__ = '1.0.2'
    __license__ = 'MIT'
    __defaults__ = {
        'enabled': False,
    }

    def __init__(self):
        self.options = dict()
        self.running = False

    def on_loaded(self):
        self.log.info("MAC Address Logger Plugin loaded")
        self.running = True

    def on_handshake(self, agent, filename, access_point,client_station):
        self.log.info(f"Handshake captured from {access_point['station']}")
        self.log.info(f"MAC Address: {access_point['station']}")
        # You can save or log this MAC address as needed

    def on_unload(self, ui):
        self.log.info("MAC Address Logger Plugin unloaded")
        self.running = False

import nmap
import pwnagotchi.plugins as plugins

class NetworkMapper(plugins.Plugin):
    __author__ = 'Deus Dust'
    __version__ = '1.0.2'
    __license__ = 'MIT'
    __defaults__ = {
        'enabled': False,
    }
    def __init__(self):
        self.options = dict()
        self.running = False

    def scan_network(self):
        nm = nmap.PortScanner()
        nm.scan(hosts='192.168.1.0/24', arguments='-sn') # todo allow user to change in config.toml
        return nm.all_hosts()

    def on_loaded(self):
        self.log.info("Network Mapper Plugin loaded")
        self.running = True

    def on_periodic(self, agent):
        hosts = self.scan_network()
        self.log.info("Discovered hosts:")
        for host in hosts:
            self.log.info(f"Host: {host}")

    def on_unload(self, ui):
        self.log.info("Network Mapper Plugin unloaded")
        self.running = False
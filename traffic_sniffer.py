import scapy.all as scapy
import pwnagotchi.plugins as plugins

class TrafficSniffer(plugins.Plugin):
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
        self.log.info("Traffic Sniffer Plugin loaded")
        self.running = True

    def packet_handler(self, packet):
        # Customize packet handling logic here
        print(packet.summary())

    def start_sniffing(self):
        scapy.sniff(prn=self.packet_handler, store=False)

    def on_periodic(self, agent):
        self.start_sniffing()

    def on_unload(self, ui):
        self.log.info("Traffic Sniffer Plugin unloaded")
        self.running = False

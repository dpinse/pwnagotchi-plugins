import scapy.all as scapy
import pwnagotchi.plugins as plugins

class NetworkIntrusionDetector(plugins.Plugin):
    __author__ = 'Deus Dust'
    __version__ = '1.0.2'
    __license__ = 'MIT'
    __defaults__ = {
        'enabled': False,
    }

    def __init__(self):
        self.options = dict()
        self.running = False

    def packet_handler(self, packet):
        # Voer hier aangepaste logica uit voor het detecteren van indringing
        if packet.haslayer(scapy.IP):
            ip_src = packet[scapy.IP].src
            ip_dst = packet[scapy.IP].dst
            self.log.info(f"Intrusion detected: {ip_src} -> {ip_dst}")

    def start_sniffing(self):
        scapy.sniff(prn=self.packet_handler, store=False)

    def on_loaded(self):
        self.log.info("Network Intrusion Detector Plugin loaded")
        self.running = True
        self.start_sniffing()

    def on_unload(self, ui):
        self.log.info("Network Intrusion Detector Plugin unloaded")
        self.running = False

import scapy.all as scapy
import pwnagotchi.plugins as plugins

class DNSSpoofDetector(plugins.Plugin):
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
        self.log.info("DNS Spoof Detector Plugin loaded")
        self.running = True

    def dns_spoof_handler(self, packet):
        if packet.haslayer(scapy.DNSRR):
            dns_response = packet[scapy.DNSRR]
            if not dns_response.rdata:
                self.log.warning("Possible DNS Spoofing Detected!")
                # Add custom logic for handling DNS spoofing detection

    def start_sniffing(self):
        scapy.sniff(filter="udp port 53", prn=self.dns_spoof_handler, store=False)

    def on_periodic(self, agent):
        self.start_sniffing()

    def on_unload(self, ui):
        self.log.info("DNS Spoof Detector Plugin unloaded")
        self.running = False


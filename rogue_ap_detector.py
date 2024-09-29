import time
import subprocess
import pwnagotchi.plugins as plugins

class RogueAPDetector(plugins.Plugin):
    __author__ = 'Deus Dust'
    __version__ = '1.0.2'
    __license__ = 'MIT'
    __defaults__ = {
        'enabled': False,
    }
    def __init__(self):
        self.options = dict()
        self.running = False

    def scan_wifi_networks(self):
        try:
            output = subprocess.check_output(["iwlist", "wlan0", "scan"])
            return output.decode('utf-8')
        except subprocess.CalledProcessError:
            self.log.error("Failed to scan WiFi networks.")
            return ""

    def on_loaded(self):
        self.log.info("Rogue AP Detector Plugin loaded")
        self.running = True

    def on_wifi_update(self, agent, access_points):
        wifi_networks = self.scan_wifi_networks()
        if wifi_networks:
            rogue_aps = self.detect_rogue_aps(wifi_networks, access_points)
            if rogue_aps:
                self.log.warning("Rogue Access Points detected:")
                for ap in rogue_aps:
                    self.log.warning(f"SSID: {ap['ssid']}, BSSID: {ap['bssid']}, Channel: {ap['channel']}")
                    agent.display_text(f"Rogue AP: {ap['ssid']}", duration=10)

    def detect_rogue_aps(self, scan_results, known_aps):
        rogue_aps = []
        for line in scan_results.split('\n'):
            if "ESSID:" in line:
                ssid = line.split('ESSID:"')[1].split('"')[0]
                bssid = line.split('Address: ')[1].strip()
                channel_line = next(filter(lambda x: x.startswith('Channel:'), line.split('\n')), None)
                if channel_line:
                    channel = int(channel_line.split('Channel:')[1].strip())
                    if not any(ap['bssid'] == bssid for ap in known_aps):
                        rogue_aps.append({"ssid": ssid, "bssid": bssid, "channel": channel})
        return rogue_aps

    def on_unload(self, ui):
        self.log.info("Rogue AP Detector Plugin unloaded")
        self.running = False
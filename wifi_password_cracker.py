import subprocess
import pwnagotchi.plugins as plugins

class WiFiPasswordCracker(plugins.Plugin):
    __author__ = 'Deus Dust'
    __version__ = '1.0.2'
    __license__ = 'MIT'
    __defaults__ = {
        'enabled': False,
    }

    def __init__(self):
        self.options = dict()
        self.running = False

    def crack_wifi_password(self, target_bssid, wordlist_path="/path/to/wordlist.txt", interface="wlan0"): #todo allow user to set dictionary in config.toml
        try:
            subprocess.run(["aircrack-ng", "-b", target_bssid, "-w", wordlist_path, "-l", "cracked.txt", interface], check=True)
            self.log.info(f"WiFi password cracked for {target_bssid}")
        except subprocess.CalledProcessError as e:
            self.log.error(f"Failed to crack WiFi password: {e}")

    def on_loaded(self):
        self.log.info("WiFi Password Cracker Plugin loaded")
        self.running = True

    def on_handshake(self, agent, filename, access_point, client_station):
        target_bssid = access_point.bssid
        self.crack_wifi_password(target_bssid)

    def on_unload(self,ui):
        self.log.info("WiFi Password Cracker Plugin unloaded")
        self.running = False


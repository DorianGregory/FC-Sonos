import urllib2
import config

config.init()

# used to control speakers
class SonosInterface:
    def __init__(self):
        self.find_zones()

    # binds players
    def find_zones(self):
        print("find_zones called")

    def play(self):
        # Plays the current track
        request("play")

    def pause(self):
        # Pauses the current track
        request("pause")

    def playpause(self):
        # Toggles the play/pause of the current track
        request("playpause")

    def next(self):
        # Plays the next song in the queue
        request("next");

    def volume(self, value):
        # Changes the volume of selected speaker
        request("volume/" + str(value))

def build_url():
    url = "http://" + config.pi_ip + ":" + str(config.port) + "/"
    return url

def request(command):
    url = build_url()
    url += config.default_speaker + "/"
    url += command
    urllib2.urlopen(url)

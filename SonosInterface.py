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
        request("play")

    def pause(self):
        request("pause")

def build_url():
    url = "http://" + config.pi_ip + ":" + str(config.port) + "/"
    return url

def request(command):
    url = build_url()
    url += config.default_speaker + "/"
    url += command
    print(url)
    urllib2.urlopen(url)

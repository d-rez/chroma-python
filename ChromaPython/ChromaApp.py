import requests
from .ChromaBinary import ChromaBcaHandler
from .ChromaDevices import Keyboard, Mouse, Mousepad, ChromaLink, Headset
from .ChromaDatatypes import Heartbeat, ChromaAppInfo


class ChromaApp:
    def __init__(self, Info: ChromaAppInfo):
        try:
            url = 'http://localhost:54235/razer/chromasdk'

            data = {
                "title": Info.Title,
                "description": Info.Description,
                "author": {
                    "name": Info.DeveloperName,
                    "contact": Info.DeveloperContact
                },
                "device_supported": Info.SupportedDevices,
                "category": Info.Category
            }
            self.rsession = requests.Session()
            response = self.rsession.post(url=url, json=data)
            self.SessionID, self.URI = response.json()['sessionid'], response.json()['uri']
            self.heartbeat = Heartbeat(self.URI)
            self.Keyboard = Keyboard(self.URI,self.rsession)
            self.Mouse = Mouse(self.URI,self.rsession)
            self.Mousepad = Mousepad(self.URI,self.rsession)
            self.Headset = Headset(self.URI,self.rsession)
            self.ChromaLink = ChromaLink(self.URI,self.rsession)
            self.BcaHandler = ChromaBcaHandler()
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def Version(self):
        try:
            return requests.get(url='http://localhost:54235/razer/chromasdk').json()['version']
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def __del__(self):
        print('Im dying')
        self.heartbeat.stop()

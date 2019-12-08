from .mapbox.Country import Country
import requests

class RequestMapbox(Country):
    '''
    exp
    '''

    def __init__(self):
        super().__init__()
        self.features = requests.get(self.url).json()['features']

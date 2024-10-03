import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.getenv('SHEETY_USERNAME')
        self._password = os.getenv('SHEETY_PASSWORD')
        self.destination_data= {}
        self.auth = HTTPBasicAuth(self._user, self._password)

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self.auth)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'city': city['city'],
                    'iataCode': city['iataCode'],
                    'lowestPrice': city['lowestPrice']
                }
            }
            requests.put(url=f'{SHEETY_ENDPOINT}/{city['id']}',json=new_data, auth=self.auth)



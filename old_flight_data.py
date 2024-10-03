
import requests
from flight_search import FlightSearch


FLIGHT_OFFERS_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

class FlightData(FlightSearch):
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        super().__init__()
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date,
        self.return_date = return_date
    def find_cheapest_flight(self):

        header = {
            'Authorization': f"Bearer {self._token}"
        }
        parameters ={
            'originLocationCode': self.origin_airport,
            'destinationLocationCode': self.destination_airport,
            'departureDate': self.out_date,
            'returnDate': self.return_date,
            'adults': 1,
            'nonStop': 'true',
            'currencyCode': 'GBP',
            'max': 10
        }
        try:
            response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, params=parameters, headers=header)
            market_price = response.json()['data'][0]['price']['grandTotal']
        except IndexError:
            return 'N/A'
        except KeyError:
            return 'N/A'
        else:
            return market_price



#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import timedelta, datetime
import time
from pprint import pprint

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
twilio = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA= 'LON'

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        # slowing down requests to avoid rate limit
        time.sleep(2)
pprint(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights ====================
tomorrow =datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6*30)
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        tomorrow,
        six_month_from_today
    )
    # print(flights)
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != 'N/A' and cheapest_flight.price < destination['lowestPrice']:
        print(f"{destination['city']}: £{cheapest_flight.price}")
        message = (f"Low price alert! Only £{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} "
                   f"to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} "
                   f"until {cheapest_flight.return_date}")
        twilio.send_whatsapp(message)
    # Slowing down requests to avoid rate limit
    time.sleep(2)












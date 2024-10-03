Flight Price Tracker

A Python-based flight price tracking system that allows users to search for flight offers and receive notifications when specific conditions are met (such as a price drop or specific flight availability). This project integrates flight search functionalities with price tracking to notify users of the best deals.

Project Overview
This project consists of several Python modules that handle the retrieval, storage, and notification of flight offers. It uses external APIs to gather flight data and processes it to provide users with relevant information. The project is divided into the following key components:

Key Components
data_manager.py: Handles storage and management of flight data. This module is responsible for loading, saving, and updating the local flight offer data.

flight_data.py: Contains the flight data model that is used to represent and work with flight offers. It includes functionality to parse and store data about flights, including pricing and itineraries.

flight_search.py: Interacts with flight APIs to search for flight offers based on user-defined criteria. It fetches flight data like prices, departure times, airlines, and more, and prepares the results for further processing.

main.py: The main entry point of the application. It coordinates the interaction between the flight search, data management, and notification systems, ensuring the proper workflow is followed (e.g., fetching data, comparing prices, sending notifications).

notification_manager.py: Handles the sending of notifications to users, such as email alerts or other forms of communication, when flight offers meet the set conditions (such as a price drop or availability of a flight).

old_flight_data.py: Stores previous flight data to compare with new offers, allowing for tracking price changes over time.

data.json: A sample dataset that contains flight offer data in JSON format. This dataset is likely used for testing purposes and consists of detailed information about flights, including itineraries, prices, and airlines​.

Prerequisites
Python 3.x
External API access (for flight search functionality)
Necessary Python libraries (requests, json, etc.)
Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/flight-price-tracker.git
cd flight-price-tracker
```
2. Install the required Python dependencies:
```
pip install -r requirements.txt
```
3. Configure your API keys for the flight search services in flight_search.py.

Usage
1. Run the application from the main.py file:
```
python main.py
```
2. The program will search for flights based on the criteria you define in the configuration and will notify you if any offers meet your conditions.

3. Customize flight search parameters in flight_search.py to adjust the search to your needs, such as origin and destination codes, departure dates, and number of passengers.

Features
Flight Search: Search for flights using the integrated flight API, filter by specific criteria such as non-stop flights, airline preference, etc.
Price Tracking: Track flight prices over time and compare them with previous data to identify any drops or increases.
Notifications: Get notified via email or other channels when a flight price drops or a specific flight offer becomes available.
Flight Data Storage: Efficiently manage and store flight data to allow price comparisons over time.
Example
Here’s an example of a flight offer retrieved from data.json:
```
{
  "type": "flight-offer",
  "id": "1",
  "itineraries": [
    {
      "duration": "PT1H20M",
      "segments": [
        {
          "departure": { "iataCode": "LGW", "at": "2024-09-22T19:45:00" },
          "arrival": { "iataCode": "ORY", "at": "2024-09-22T22:05:00" }
        }
      ]
    }
  ],
  "price": { "currency": "GBP", "total": "253.58" },
  "travelerPricings": [
    {
      "fareOption": "STANDARD",
      "price": { "currency": "GBP", "total": "253.58" }
    }
  ]
}
```
Contributing
If you want to contribute to this project, feel free to open an issue or submit a pull request. Please make sure to follow the coding standards and write clear commit messages.

License
This project is licensed under the MIT License - see the LICENSE file for details.



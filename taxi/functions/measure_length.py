from geopy import (
    geocoders,
    distance,
    )

geolocator = geocoders.Nominatim(user_agent="Taxi")

class Distance:
    """Returns distance between to cities."""
    def __init__(self, first_city, second_city):
        self.first_city = first_city
        self.second_city = second_city

    def city_coordinates(self, city_name):
        location = geolocator.geocode(city_name)
        coordinates = (location.latitude, location.longitude)

        return coordinates

    def distance(self, first_city, second_city):
        first_city = self.city_coordinates(first_city)
        second_city = self.city_coordinates(second_city)

        distance_between_cities = distance.distance(first_city, second_city).kilometers

        return distance_between_cities
    
    def price(self):
        distance1 = self.distance(self.first_city, self.second_city)

        oil_price = 4
        price = distance1 / 10 * oil_price + 100 + 100

        return int(price)

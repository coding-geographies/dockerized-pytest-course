
class Point():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

        if not (-90 <= latitude <= 90) or not (-90 <= longitude <= 90):
            raise ValueError("Invalid latitude or longitude")

        if type(name) != "str": #if not isisnstance(name, str)
            raise TypeError("Invalid type for city name, must be string")

    def get_lat_long(self):
        return (self.latitude, self.longitude)


class Point():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


    def get_lat_long(self):
        return (self.latitude, self.longitude)

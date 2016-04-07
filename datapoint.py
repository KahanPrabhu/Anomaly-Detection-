class DataPoint:
    def __init__(self, year, temperature, lat, lon, day, score=0):
        self.__year = year
        self.__temperature = temperature
        self.__lat = lat
        self.__lon = lon
        self.__day = day
        self.neighbors = []
        self.score = score

    def getYear(self):
        return self.__year

    def getTemperature(self):
        return self.__temperature

    def getLatitude(self):
        return self.__lat

    def getLongitude(self):
        return self.__lon

    def getDay(self):
        return self.__day

    def __repr__(self):
        return "DataPoint(%d, %f, %f)" % (self.__year, self.__temperature, self.score)

#    def __lt__(self, other):
#        return self.score < other.score

class DataPoint:
    def __init__(self, year, temperature, score=0):
        self.__year = year
        self.__temperature = temperature
        self.neighbors = []
        self.score = score

    def getYear(self):
        return self.__year

    def getTemperature(self):
        return self.__temperature

    def __repr__(self):
        return "DataPoint(%d, %f, %f)" % (self.__year, self.__temperature, self.score)

#    def __lt__(self, other):
#        return self.score < other.score

import datetime
import csv
from netCDF4 import Dataset
import numpy as np

class LoadCDFData:
    """
    A class that is used to read the .nc netCDF4 data. Using this class,
    we can get longitude, latitude, temperature data, and time data. All
    it needs is a file path and usually an index.
    """
    def __init__(self, file):
        """
        Constructor for the class. Accepts a filename
        and automatically loads that file.
        """
        # Set the class variable for the file to read.
        self.__fileName = file
        # Call private method to load file information.
        self.__loadFileInfo()

    @staticmethod
    def convertClimateDate(inputHours):
        """
        Static method for converting from the date format in the data
        to the date format acceptable to Python.
        @type  inputHours: int
        @param inputHours: The number of hours as specified by the climate
                           data.
        @rtype:            datetime.Date
        @return:           A Date object that is compatible with Python.
        """
        # Set the initial date as defined by the climate data.
        initialDate = datetime.date(1800, 01, 01)
        # The date format in the climate data is just a count of hours
        # since 1800-01-01. Just add those hours to our initial date.
        diffInterval = datetime.timedelta(hours=inputHours)
        # Return the resulting Date object.
        return initialDate + diffInterval

    def __loadFileInfo(self):
        """
        A private method for loading the data from the file.
        Needs better exception handling.
        """
        # Open file for reading.
        with open(self.__fileName, 'rb') as fileHandler:
            self.data = []
            reader = csv.reader(fileHandler, delimiter=',', quotechar='|')

            for entry in reader:
                self.data.append(entry)

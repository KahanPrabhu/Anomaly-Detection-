import datetime
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
        try:
            # Open file for reading.
            fileHandler = Dataset(self.__fileName, mode='r')
            # Try to get the appropriate data from the
            # file. Make copies of this data and store it in class
            # variables.
            self.__lons = fileHandler.variables['lon'][:]
            self.__lats = fileHandler.variables['lat'][:]
            self.__airs = fileHandler.variables['air'][:]
            self.__times = fileHandler.variables['time'][:]
        except RuntimeError as e:
            # RuntimeError in this case is usually indicative of
            # a problem opening the file.
            print "Error opening file. Does it exist?"
        except KeyError as e:
            # A KeyError in this case is usually indicative of the
            # specified variables/columns not existing in the data file.
            print "Error getting column data from the data file."
            print "Is it the right format?"

    def getLongitude(self, idx):
        """
        Gets the longitude at the specified index of the data.
        @type  idx: int
        @param idx: The index to get the data at.
        @rtype:     float
        @return:    The longitude stored at the index.
        """
        return self.__lons[idx]

    def getLatitude(self, idx):
        """
        Gets the latitude at the specified index of the data.
        @type  idx: int
        @param idx: The index to get the data at.
        @rtype:     float
        @return:    The latitude stored at the index.
        """
        return self.__lats[idx]

    def getAirTemperature(self, idx):
        """
        Gets the air temperature at the specified index of the data.
        @type  idx: int
        @param idx: The index to get the data at.
        @rtype:     numpy.ndarray
        @return:    The air temperature data stored at the index for the day.
        """
        return self.__airs[idx]

    def getTime(self, idx):
        """
        Gets the date for the specified index of the data.
        @type  idx: int
        @param idx: The index to get the data at.
        @rtype:     datetime.Date
        @return:    The date stored at the index.
        """
        return LoadCDFData.convertClimateDate(self.__times[idx])

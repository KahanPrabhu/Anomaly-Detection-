from loadData import LoadCDFData
from orca import *

def setupData(time, lat, lon):
    myDictionary = {};
    # + 1 for non-inclusive loop.
    for year in xrange(1979, 2013 + 1):
        cdfData = LoadCDFData('/home/csc422/422Data/air.sig995.' + str(year) + '.nc')
        myDictionary[year] = cdfData.getAirTemperature(time)[lat][lon]
    return myDictionary

sampleData = setupData(0, 0, 0)
orca(4, 2, sampleData)

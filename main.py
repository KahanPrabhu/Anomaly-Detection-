from loadData import LoadCDFData
from orca import *

def setupData(time, lat, lon):
    myList = []
    # + 1 for non-inclusive loop.
    for year in xrange(1979, 2013 + 1):
        cdfData = LoadCDFData('/home/csc422/422Data/air.sig995.' + str(year) + '.nc')
        dp = DataPoint(year, cdfData.getAirTemperature(time)[lat][lon])
        myList.append(dp)
    return myList

#def dump(data):
#    for dp in data:
#        print "%d,%f" % (dp.getYear(), dp.getTemperature())

#sampleData = setupData(0, 0, 0)
#print orca(4, 2, sampleData)

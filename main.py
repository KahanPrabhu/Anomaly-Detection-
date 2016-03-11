from loadData import LoadCDFData

def setupData(time, lat, lon):
    myList = []
    # + 1 for non-inclusive loop.
    for year in xrange(1979, 2013 + 1):
        cdfData = LoadCDFData('/home/csc422/422Data/air.sig995.' + str(year) + '.nc')
        myList.append(cdfData.getAirTemperature(time)[lat][lon])
    return myList

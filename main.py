from loadData import LoadCDFData
from orca import *
import pprocess

NUM_TOP_ANOMALIES = 5

def setupData(day, lat, lon):
    myList = []
    csvdata = LoadCDFData('/home/csc422/csvdata/lat' + str(lat) + 'lon' + str(lon) + '.csv')
    for year in xrange(0, 35):
        dp = DataPoint(year, lat, lon, day, float(csvdata.data[year][day]))
        myList.append(dp)
    return myList

def main():
    results = pprocess.Map(limit = 4)
    modOrca = results.manage(pprocess.MakeParallel(orca))
    for lat in xrange(0, 10):
        for lon in xrange(0, 10):
            for day in xrange(0, 365):
                data = setupData(day, lat, lon)
                modOrca(7, 5, data)

    return results

#def dump(data):
#    for dp in data:
#        print "%d,%f" % (dp.getYear(), dp.getTemperature())


#sampleData = setupData(0, 0, 1)
#print sampleData
#print orca(4, 2, sampleData)

from loadData import LoadCDFData
from orca import *
import csv
import pprocess

NUM_TOP_ANOMALIES = 5

def setupData(day, lat, lon):
    myList = []
    csvdata = LoadCDFData('/home/csc422/csvdata/lat' + str(lat) + 'lon' + str(lon) + '.csv')
    for year in xrange(0, 35):
        dp = DataPoint(year, float(csvdata.data[year][day]), lat, lon, day)
        myList.append(dp)
    return myList


def main():
    outerResults = []
    for lat in xrange(0, 5):
        for lon in xrange(0, 5):
            innerResults = []
            innerResults = pprocess.Map(limit = 4)
            modOrca = innerResults.manage(pprocess.MakeParallel(orca))
            for day in xrange(0, 365):
                data = setupData(day, lat, lon)
                innerResults.append(orca(7, 5, data))
                modOrca(7, 5, data)

#            print "InnerResults: " + str(innerResults[0][0].score)
            # topNumber is 5% of the total number of anomalies returned at
            # one location.
            topNumber = 91
            finalResults = []
            topResults = []
            for resultList in innerResults:
                for oneResult in resultList:
                    outerResults.append(oneResult)
                    # topResults is storage for finding the top 5%.
                    topResults.append(oneResult)

#            print "TopResults: " + str(topResults[0].score)
            sortedResults = sorted(topResults, key=lambda dp: dp.score, reverse=True)
#            print "SortedResults: " + str(sortedResults[0].score)

            for idx in xrange(0, topNumber):
                finalResults.append(sortedResults[idx])

            with open('/home/csc422/topcsvdata/lat' + str(lat) + 'lon' + str(lon) + '.csv', 'w+') as myFile:
                fieldnames = ['Year', 'Day', 'Temperature', 'Score']
                writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                writer.writerow(fieldnames)
                for result in finalResults:
                    row = [1979 + result.getYear(), result.getDay(), result.getTemperature(), result.score]
                    writer.writerow(row)

    return outerResults

#def dump(data):
#    for dp in data:
#        print "%d,%f" % (dp.getYear(), dp.getTemperature())


#sampleData = setupData(0, 0, 1)
#print sampleData
#print orca(4, 2, sampleData)

from loadData import LoadCDFData
from orca import *
import csv
import pprocess

NUM_TOP_ANOMALIES = 5

def setupData(day, lat, lon):
    myList = []
    csvdata = LoadCDFData('csvdata/' + 'lat' + str(lat) + 'lon' + str(lon) + '.csv')
    for year in xrange(0, 35):
        dp = DataPoint(year, float(csvdata.data[year][day]), lat, lon, day)
        myList.append(dp)
    return myList


def main(latLowRange, latHighRange, lonLowRange, lonHighRange, direc, count):
    outerResults = []
    for lat in xrange(latLowRange, latHighRange):
        for lon in xrange(lonLowRange, lonHighRange):
            innerResults = pprocess.Map(limit = 4)
            modOrca = innerResults.manage(pprocess.MakeParallel(orca))
            for day in xrange(0, 365):
                data = setupData(day, lat, lon)
                modOrca(7, 5, data)

            # topNumber is 5% of the total number of anomalies returned at
            # one location.
            topNumber = 638 # 365*35*0.05
            finalResults = []
            topResults = []
            for resultList in innerResults: # This line causes error.
                for oneResult in resultList:
                    dp = (oneResult.getYear(), oneResult.getTemperature(), oneResult.getLatitude(), oneResult.getLongitude(), oneResult.getDay(), oneResult.score)
                    outerResults.append(dp)
                    # topResults is storage for finding the top 5%.
                    topResults.append(dp)

            topResults = sorted(topResults, key=lambda dp: dp[5], reverse=True)

            for idx in xrange(0, topNumber):
                finalResults.append(topResults[idx])

            with open(direc + 'lat' + str(lat) + 'lon' + str(lon) + '.csv', 'w+') as myFile:
                fieldnames = ['Year', 'Day', 'Temperature', 'Score']
                writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                writer.writerow(fieldnames)
                for result in finalResults:
                    row = [1979 + result[0], result[4], result[1], result[5]]
                    writer.writerow(row)

    topNumber = int(365*35*0.05*(latHighRange - latLowRange)*(lonHighRange - lonLowRange)) # 365*35*0.05*73*144
    finalOuterResults = []
    outerResults = sorted(outerResults, key=lambda dp: dp[5], reverse=True)
    for idx in xrange(0, topNumber):
        finalOuterResults.append(outerResults[idx])

    with open(direc + 'OuterResults' + str(count) + '.csv', 'w+') as myFile:
        #fieldnames = ['Lat', 'Lon', 'Year', 'Day', 'Temperature', 'Score']
        writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        #writer.writerow(fieldnames)
        for result in finalOuterResults:
            row = [result[2], result[3], 1979 + result[0], result[4], result[1], result[5]]
            writer.writerow(row)

    return finalResults

#def dump(data):
#    for dp in data:
#        print "%d,%f" % (dp.getYear(), dp.getTemperature())


#sampleData = setupData(0, 0, 1)
#print sampleData
#print orca(4, 2, sampleData)

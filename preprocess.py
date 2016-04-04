from loadData import LoadCDFData
import csv

dateMin = 1979
dateMax = 2013
directory = '/home/csc422/data/'
outputDir = '/home/csc422/csvdata/'

def preprocess():
    cdfData = []
    for year in xrange(dateMin, dateMax + 1):
        loadedData = LoadCDFData(directory + 'air.sig995.' + str(year) + '.nc')
        cdfData.append(loadedData)

    for day in xrange(0, 365 + 1):
        if day == 59:
            #Skip leap year day February 29.
            continue

        with open(outputDir + 'data' + str(day) + '.csv', 'w+') as myFile:
            writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for lat in xrange(0, 72 + 1):
                for lon in xrange(0, 143 + 1):
                    row = []
                    for year in xrange(0, (dateMax - dateMin) + 1):
                        row.append(cdfData[year].getAirTemperature(day)[lat][lon])
                    writer.writerow(row)

preprocess()

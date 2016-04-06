from loadData import LoadCDFData
import pdb
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

    for lat in xrange(0, 72 + 1):
        for lon in xrange(0, 143 + 1):
            with open(outputDir + 'lat' + str(lat) + 'lon' + str(lon) + '.csv', 'w+') as myFile:
                writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                for year in xrange(0, (dateMax - dateMin) + 1):
                    numDays = 364
                    if (dateMin + year) % 4 == 0:
                        numDays = 365

                    row = []
                    for day in xrange(0, numDays + 1):
                        if numDays == 365 and day == 59:
                            continue

                        row.append(cdfData[year].getAirTemperature(day)[lat][lon])
                    writer.writerow(row)

preprocess()

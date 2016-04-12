import csv
from datapoint import DataPoint

topFile = '/home/csc422/topcsvdata/'
destinationFile = '/home/csc422/topcsvmatrices/'

def postprocess():
    dataPoints = []
    with open(topFile + 'OuterResults.csv', 'r') as myFile:
        reader = csv.reader(myFile, delimiter=',', quotechar='|')
        reader.next()

        for row in reader:
            dp = DataPoint(int(row[2]), float(row[4]), int(row[0]), int(row[1]), int(row[3]), float(row[5]))
            dataPoints.append(dp)

    for year in xrange(0, 35):
        for day in xrange(0, 365):
            with open(destinationFile + str(year) + '-' + str(day) + '.csv', 'w+') as myFile:
                writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                for lat in xrange(0, 72):
                    row = []
                    for lon in xrange(0, 144):
                        anomaly = 0
                        # Search for any matching datapoints with the corresponding
                        # year, day, latitude, and longitude.
                        for point in dataPoints:
                            if point.getYear() == (year + 1979) and point.getDay() == day and point.getLatitude() == lat and point.getLongitude() == lon:
                                row.append(point.getTemperature())
                                anomaly = 1
                                break

                        if anomaly == 0:
                            row.append(0)

                    writer.writerow(row)

postprocess()

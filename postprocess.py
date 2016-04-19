import csv
import pandas as pd
import numpy as np

topFile = 'topcsvdata/'
destinationFile = 'topcsvmatrices/'
lines = 6690906 # Number of lines. You have to count this yourself.

def postprocess():
    # Keep a counter for the current line that we're at.
    currentLine = 0
    # Initialize tabular data with zeros. This is basically pre-allocating our data.
    # Tabular data = data with rows and columns. Think of a SQL table.
    data = np.zeros((lines,), dtype=[('Year', 'int'),('Day', 'int'),('Lat', 'int'),('Lon', 'int')])
    # Open our outer results file.
    with open(topFile + 'OuterResults.csv', 'r') as myFile:
        # Open a CSV reader on the file handler.
        reader = csv.reader(myFile, delimiter=',', quotechar='|')

        for row in reader:
            # Put data in our pre-allocated tabular data.
            data[currentLine] = (int(row[2]), int(row[3]), int(row[0]), int(row[1]))
            # Increment our line counter.
            currentLine = currentLine + 1

    # Put all of our data into a pandas dataframe.
    # This is the equivalent of a SQL table pretty much.
    dataF = pd.DataFrame(data)

    # For every year...
    for year in xrange(0, 35):
        # For every day in this year...
        for day in xrange(0, 365):
            # Open a destination file. Format is year-day.
            with open(destinationFile + str(year) + '-' + str(day) + '.csv', 'w+') as myFile:
                # Open a CSV writer on our file handler.
                writer = csv.writer(myFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                print "Checking Year" + str(year) + ", day" + str(day)

                # Divide our anomalies into a smaller chunk by year and day.
                smallDF = dataF[((dataF['Year'] == (year + 1979)) & (dataF['Day'] == day))]

                # For every latitude in this day of this year...
                for lat in xrange(0, 72):
                    # Output row to be written by the CSV writer.
                    row = []

                    # Divide our divided data into an even smaller chunk by latitude.
                    smallerDF = smallDF[((smallDF['Lat'] == lat))]

                    # For every longitutde of this latitude of this day of this year...
                    for lon in xrange(0, 144):
                        # Initially, there is no anomaly at this location at this time.
                        anomaly = 0

                        # If we find any entries with the specified longitude...
                        if (((smallerDF['Lon'] == lon))).any():
                            # There is an anomaly there.
                            anomaly = 1

                        # Append to our output row whether or not there was an anomaly.
                        row.append(str(anomaly))

                    # Write the output row out.
                    writer.writerow(row)

# Initiate our script.
postprocess()

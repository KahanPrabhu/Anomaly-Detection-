from loadData import LoadCDFData

def myDemo():
    """
    A demo to show that my loadData class works for parsing
    the data files! It creates a table that is identical to the
    Panoply table.
    """

    # Load the CDF Data.
    myCDFData = LoadCDFData('/home/csc422/422Data/air.sig995.1948.nc')

    # There are always 73 latitudes (0 ... 72)
    # There are always 144 longitudes (0 ... 143)
    # There are always 10512 air temperatures in a *single index array*
    # since 72 * 143 = 10512.
    # There are always 366 air temperature arrays.
    # There are are always 366 dates (0 ... 365)

    print "For the date: %s" % (myCDFData.getTime(0).isoformat())

    # First, indent the data with a tab, then print all latitudes.
    print "\t\t",
    for i in xrange(72):
        print "%f\t" % (myCDFData.getLatitude(i)),

    # Now print a newline.
    print ""

    # Now print a longitude and then all the air temperatures
    for j in xrange(144):
        # Print the longitude.
        print "%f\t" % (myCDFData.getLongitude(j)),
        for k in xrange(72):
            # Print each air temperature.
            print "%f\t" % (myCDFData.getAirTemperature(0)[k][j]),
        # End the row by printing a newline.
        print ""

# Call the demo
myDemo()

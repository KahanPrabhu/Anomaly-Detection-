from loadData import LoadCDFData
import operator

BLOCK_SIZE = 7

# x = one point in the dataset
# k = number of nearest neighbors
# Y = subset of dataset
def closest(x, Y, k):
    if len(Y) <= k:
        pass
    else:
        try:
            del Y[maxDistanceYear(x, Y)]
        except KeyError:
            # If it doesn't exist, don't delete anything.
            pass

def maxDistanceYear(x, Y):
    maxDiffYear = 0
    maxDiff = 0
    for year, temperature in Y.iteritems():
        challengerDiff = abs(x - year)
        if maxDiff < challengerDiff:
            maxDiff = challengerDiff
            maxDiffYear = year
    return maxDiffYear

def maxDistance(x, Y):
    maxDiff = 0
    for year, temperature in Y.iteritems():
        challengerDiff = abs(x - year)
        if maxDiff < challengerDiff:
            maxDiff = challengerDiff
    return maxDiff

def getNextBlock(Y):
    block = {}
    for x in xrange(BLOCK_SIZE):
        year, temperature = Y.popitem()
        block[year] = temperature
    return block

def score(Y, x):
    total = 0
    for year, temperature in Y.iteritems():
        total += abs(temperature - x)
    return total / float(len(Y))

def getTopOutliers(Y, n):
    return_dict = {}
    sorted_score = sorted(Y.items(), key=operator.itemgetter(1))

    for idx in xrange(len(Y) - n):
        del Y[sorted_score[idx][0]]
    return Y

# k = number of nearest neighbors
# n = number of outliers to return
# dataset = dataset
def orca(k, n, dataset):
    c = 0
    O = {}
    dataset_2 = dict(dataset)
    while len(dataset_2) > 0:
        B = getNextBlock(dataset_2)
        B_score = {}
        B_copy = B.copy()
        for d_year, d_temperature in dataset.iteritems():
            for b_year, b_temperature in B_copy.iteritems():
                neighbors = {}
                if b_year == d_year:
                    continue

                if len(neighbors) < k or abs(b_year - d_year) < maxDistance(b_year, neighbors):
                    neighbors[d_year] = d_temperature
                    closest(b_year, neighbors, k)

                    calcScore = score(neighbors, b_year)
                    if calcScore < c:
                        del B[b_year]
                    else:
                        B_score[b_year] = calcScore

        B_u_O = B_score.copy()
        B_u_O.update(O)

        O = getTopOutliers(B_u_O, n)
        c = min(O.values())
    return O

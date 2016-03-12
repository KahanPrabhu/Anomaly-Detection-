from loadData import LoadCDFData
from datapoint import DataPoint

BLOCK_SIZE = 7

# x = one point in the dataset
# k = number of nearest neighbors
# Y = subset of dataset
def closest(x, Y, k):
    if len(Y) <= k:
        return None
    else:
        try:
            Y.remove(maxDistanceYear(x, Y))
        except ValueError:
            # If it doesn't exist, don't delete anything.
            return None

def maxDistanceYear(x, Y):
    maxDiffDP = None
    maxDiff = 0
    for dp in Y:
        challengerDiff = abs(x - dp.getYear())
        if maxDiff < challengerDiff:
            maxDiff = challengerDiff
            maxDiffDP = dp
    return maxDiffDP

def maxDistance(x, Y):
    maxDiff = 0
    for dp in Y:
        challengerDiff = abs(x - dp.getYear())
        if maxDiff < challengerDiff:
            maxDiff = challengerDiff
    return maxDiff

def getNextBlock(Y):
    block = []
    for x in xrange(BLOCK_SIZE):
        block.append(Y.pop())
    return block

def score(Y, x):
    total = 0
    for dp in Y:
        total += abs(x - dp.getTemperature())
    return total / float(len(Y))

def getTopOutliers(Y, n):
    return_list = []
    sorted_score = sorted(Y, key=lambda dp: dp.score)

    for idx in xrange(len(Y) - n):
        del sorted_score[0]
    return sorted_score

def mergeUnique(f, s):
    fs = set(f)
    ss = set(s)

    diff = ss - fs

    return f + list(diff)

# k = number of nearest neighbors
# n = number of outliers to return
# dataset = dataset
def orca(k, n, dataset):
    c = 0
    O = []
    dataset_2 = dataset[:]
    while len(dataset_2) > 0:
        B = getNextBlock(dataset_2)
        for d in dataset:
            for b in B[:]:
                if b.getYear() == d.getYear():
                    continue

                if len(b.neighbors) < k or abs(b.getYear() - d.getYear()) < maxDistance(b.getYear(), b.neighbors):
                    B_u_d = b.neighbors[:]
                    B_u_d.append(d)

                    closest(b.getYear(), B_u_d, k)
                    b.neighbors = B_u_d

                    calcScore = score(b.neighbors, b.getTemperature())
                    if calcScore < c:
                        B.remove(b)
                    else:
                        b.score = calcScore


        B_u_O = mergeUnique(B, O)

        O = getTopOutliers(B_u_O, n)
        c = min(O, key=lambda dp: dp.score)
    return O

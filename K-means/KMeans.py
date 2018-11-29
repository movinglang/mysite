import numpy as np

def kmeans(X, k, maxIt):
    numPonits, numDim = X.shape

    dataSet = np.zeros((numPonits, numDim+1))
    dataSet[:, :-1] = X

    # initalize centroids randomly
    centroids = dataSet[np.random.randint(numPonits, size=k), :]
    centroids[:, -1] = range(1, k+1)

    # initialize book keeping yars
    iterations = 0
    oldCentriods = None

    # run the main k-means algorithm
    while not shouldStop(oldCentriods, centroids, iterations, maxIt):
        print("iterations:", iterations)
        print("dataSet:", dataSet)
        print("centroids:", centroids)
        # save old centriods for convergence test.
        oldCentriods = np.copy(centroids)
        iterations += 1

        updateLabels(dataSet, centroids)

        centroids = getCentroids(dataSet, k) #获得新的中心点

    return dataSet

def shouldStop(oldCentriods, centroids, iterations, maxIt):
    if iterations > maxIt:
        return True
    return np.array_equal(oldCentriods, centroids)

def updateLabels(dataSet, centroids):
    numPoints, numDim = dataSet.shape
    for i in range(0, numPoints):
        dataSet[i, -1] = getLabelFromCentroid(dataSet[i, :-1],centroids)

def getLabelFromCentroid(dataSetRow, centroids):
    label = centroids[0, -1]
    minDist = np.linalg.norm(dataSetRow - centroids[0, :-1])
    for i in range(1, centroids.shape[0]):
        dist = np.linalg.norm(dataSetRow - centroids[i, :-1])
        if dist < minDist:
            minDist = dist
            label = centroids[i, -1]
    print("minDist:", minDist)
    return label

def getCentroids(dataSet, k):
    result = np.zeros((k,dataSet.shape[1]))
    for i in range(1, k+1):
        oneCluster = dataSet[dataSet[:, -1]==i, :-1]
        print("one:",oneCluster)
        result[i -1,:-1] = np.mean(oneCluster, axis=0)#axis=0压缩行对列求平均值
        result[i-1,-1] = i

    return result


x1 = np.array([1,1])
x2 = np.array([2,1])
x3 = np.array([4,3])
x4 = np.array([5,4])
testX = np.vstack((x1, x2, x3, x4))

result = kmeans(testX, 2 ,10)
print("final result")
print(result)
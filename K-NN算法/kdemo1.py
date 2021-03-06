import csv
import random
import math
import operator

def loadDataset(filename, spilt, trainingSet=[], testSet=[]):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < spilt:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distance = []
    length = len(testInstance) -1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))
    distance.sort(key=operator.itemgetter(1))
    # print(distance)

    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes ={}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    trainingSet = []
    testSet = []
    split = 0.7
    loadDataset('irisdata.txt', split, trainingSet, testSet)
    print('Train set:' + repr(len(trainingSet)))
    print('Test set:'+repr(len(testSet)))
    predictions = []
    k = 3
    correct = []
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        # print(neighbors)
        result = getResponse(neighbors)
        print(result)
        predictions.append(result)
        # print ('test: ' + repr(testSet))
        print('predictions: ' + repr(predictions))
        print('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))

        if result == testSet[x][-1]:
            correct.append(x)
            # print "len:"
            # print len(testSet)
            # print "correct:"
            # print len(correct)
    accuracy = (len(correct) / float(len(testSet))) * 100.0
    print('Accuracy: ' + repr(accuracy) + '%')


if __name__ == '__main__':
    main()

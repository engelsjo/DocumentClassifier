"""
Find the max and average effectiveness rate from a file of many trials.
"""

import sys

def readFile(fileName):
    listData = list()
    with open(fileName, 'r') as fileHandle:
        for line in fileHandle:
            line = line.strip('\n\r')
            listData.append(line)
    return listData

def calcStats(listData):
    percents = list()
    for item in listData:
        # remove last character (% sign)
        string = item[:-1]
        # convert to number
        num = int(string)
        # append to list of percents
        percents.append(num)
    # print the list of percents
    print percents
    # find the max and avg
    print "Max: ", max(percents)
    print "Avg: ", sum(percents) / len(percents)

calcStats(readFile(sys.argv[1]))

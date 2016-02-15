"""
Preprocess data for wordcloud visualization
"""

import sys

def readData(fileName):
    listData = list()
    with open(fileName, 'r') as fileHandle:
        for line in fileHandle:
            lineTokens = line.strip('\n\r').split(' ')
            listData.append(lineTokens)
    return listData

def writeData(listData, fileName):
    with open(fileName, 'w') as fileHandle:
        for item in listData:
            fileHandle.write(item)

def partitionClasses(fileName):
    # dictionary of class names to list of words
    classes = dict()
    # read in the file passed
    lines = readData(fileName)
    for line in lines:
        # get classname
        className = line[0]
        # get document name
        doc = line[1:]
        # create a dictionary of class names to all the words in those docs
        # join with space in between to separate words again
        if className not in classes:
            classes[className] = " ".join(doc)
        else:
            classes[className] += " ".join(doc)
    return classes

def outputClassData(classDict):
    for className in classDict:
        listData = []
        # add the number of words
        listData.append(str(len(classDict[className])))
        listData.append('\n')
        # add all the words in that class
        for text in classDict[className]:
            listData.append(text)
        # make the filename the class name
        fileName = 'output/wordcloud/' + str(className) + '.txt'
        # write the class's words to a file
        writeData(listData, fileName)

outputClassData(partitionClasses(sys.argv[1]))

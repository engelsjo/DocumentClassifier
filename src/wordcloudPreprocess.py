"""
Preprocess data for wordcloud visualization
"""

import sys

# class names to list of docs
classes = dict()

# read in the file passed
with open(sys.argv[1], 'rb') as fileHandler:
    for line in fileHandler:
        # strip out newline character and split on space
        lineTokens = line.strip('\n\r').split(' ')
        # get classname
        className = lineTokens[0]
        # get document name
        doc = lineTokens[1:]
        # create a dictionary of class names to all the words in those docs
        # join with space in between to separate words again
        if className not in classes:
            classes[className] = " ".join(doc)
        else:
            classes[className] += " ".join(doc)

def writeData(listData, fileName):
    with open(fileName, 'w') as fileHandle:
        for item in listData:
            fileHandle.write(item)

# for each class
for className in classes:
    listData = []
    # add the number of words
    listData.append(str(len(classes[className])))
    listData.append('\n')
    # add all the words
    for doc in classes[className]:
        listData.append(doc)
    # make the filename the class name
    fileName = 'output/wordcloud/' + str(className)
    # write the class's words to a file
    writeData(listData, fileName)

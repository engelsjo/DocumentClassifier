"""
@summary: Python script that classifies documents
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016
"""

import argparse

class DocumentType(object):

    def __init__(self):
        # the number of documents for which classification is this type
        self.count = 0
        # single text for this type (concatenation of all documents for this type)
        self.text = None



class DocumentClassifier(object):

    def __init__(self, args):
        # command line arguments for program execution
        self.args = args
        # set of unique words in training documentss
        self.vocab = set()
        # the number of training documents
        self.numTrainDocs = 0
        # dictionary of class names to document type objects
        self.classesToDocTypes = {}

    def parseFile(self, fileName, stripChars, delimiter):
        lines = []
        with open(fileName, 'rb') as fileHandler:
            for line in fileHandler:
                lineTokens = line.strip(stripChars).split(delimiter)
                lines.append(lineTokens)
        return lines

    def createVocab(self, lines):
        for line in lines:
            document = line[1:]
            # try to add each word to unique set of words (ignores duplicates)
            for word in document:
                self.vocab.add(word)

    def learn(self, fileName):
        lines = self.parseFile(fileName, '\n\r', ' ')
        self.createVocab(lines)
        # self.numTrainDocs = len(lines)
        # for j in range(0, len(lines)):
            #line = lines[j]
            #classJ = line[0]
            #documentJ = line[1:]

    def classify(self, fileName):
        x = 0

def parseCommands():
    # create argument parser
    ArgParser = argparse.ArgumentParser()
    # add positional arguments expected to run program
    ArgParser.add_argument('trainingSet',
        help='The set of data to discover potentially predictive relationships.')
    ArgParser.add_argument("testSet",
        help='The set of data used to assess the strength and utility of a predictive relationship.')
    # parse the arguments passed to program and return as a dictionary where
    # key is the argument name, and value is the argument value passed
    return vars(ArgParser.parse_args())

def main():
    dc = DocumentClassifier(parseCommands())
    dc.learn(dc.args['trainingSet'])

if __name__ == "__main__":
    main()

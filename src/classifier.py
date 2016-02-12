"""
@summary: Python script that classifies documents
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016
"""

import argparse

class Classifier(object):

    def __init__(self, arguments):
        self.arguments = arguments
        self.docTermMatrix = {}

    def parseFile(self, fileName, delimiter):
        lines = []
        with open(fileName, 'rb') as fileHandler:
            for line in fileHandler:
                lineTokens = line.strip('\n\r').split(delimiter)
                lines.append(lineTokens)
        return lines

def parseCommands():
    # create argument parser
    ArgParser = argparse.ArgumentParser()
    # add arguments expected to run program
    ArgParser.add_argument('trainingSet',
        help='The set of data to discover potentially predictive relationships.')
    ArgParser.add_argument("testSet",
        help='The set of data used to assess the strength and utility of a predictive relationship.')
    # parse the arguments passed to program and return as a dictionary where
    # key is the argument name, and value is the argument value passed
    return vars(ArgParser.parse_args())

def main():
    c = Classifier(parseCommands())
    c.parseFile(c.arguments['trainingSet'], ' ')



if __name__ == "__main__":
    main()

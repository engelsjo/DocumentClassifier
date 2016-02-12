"""
@summary: Python script that classifies documents
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016
"""

import argparse
import numpy as np
# np.set_printoptions(threshold=np.nan)

class Classifier(object):

    def __init__(self, args):
        self.args = args
        # set of unique words
        self.vocab = set()
        # two-dimensional array (matrix) of documents and terms (words)
        # self.docTermMatrix = None

    def parseTrain(self, fileName, stripChars, delimiter):
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

    """
    def createWordsToIndices(self, vocab):
        wordsToIndices = {}
        index = 0
        for word in vocab:
            if word not in wordsToIndices:
                wordsToIndices[word] = index
                index += 1
        return wordsToIndices

    def createMatrix(self, lines, numRows, numCols):
        self.docTermMatrix = np.zeros((numRows, numCols))
        wordsToIndices = self.createWordsToIndices(self.vocab)
        for i in range(0, len(lines)):
            line = lines[i]
            document = line[1:]
            for word in document:
                self.docTermMatrix[i][wordsToIndices[word]] += 1
    """

    def learn(self, fileName):
        lines = self.parseTrain(fileName, '\n\r', ' ')
        self.createVocab(lines)
        # print self.vocab

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
    c = Classifier(parseCommands())
    c.learn(c.args['trainingSet'])


if __name__ == "__main__":
    main()

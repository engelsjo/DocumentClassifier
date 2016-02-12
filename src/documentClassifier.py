"""
@summary: Implementation of Naive Bayes algorithm to classify documents.
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016
"""

import argparse
import math
import sys

# document type in a document classifier
class DocumentType(object):

    # constructor
    def __init__(self):
        # number of documents for which classification is this document type
        self.count = 0
        # probability estimate for this particular class (document type)
        self.prob = 0.0
        # single text (concatenation of all documents for this type)
        self.text = []
        # dictionary of words in text to their counts for this document type
        self.wordCounts = {}
        # dictionary of words to probability estimates of word occurrence given
        # document type
        self.wordProbs = {}

# naive bayes document classifier
class DocumentClassifier(object):

    # constructor
    def __init__(self, args):
        # command line arguments to execute program
        self.args = args
        # number of training documents
        self.numTrainDocs = 0
        # number of test documents
        self.numTestDocs = 0
        # set of unique words in training documentss
        self.vocab = set()
        # dictionary of class names to document type objects
        self.docTypes = {}
        # number of test documents correctly classified
        self.numCorrect = 0

    # parse a file into a list of lists
    def parseFile(self, fileName, chars, delimiter):
        lines = []
        with open(fileName, 'rb') as fileHandler:
            for line in fileHandler:
                lineTokens = line.strip(chars).split(delimiter)
                lines.append(lineTokens)
        return lines

    # learn how to classify a document
    def learn(self, fileName):
        lines = self.parseFile(fileName, '\n\r', ' ')
        # since each line is a training document, parse it
        for line in lines:
            className = line[0]
            doc = line[1:]
            self.parseTrainDoc(className, doc)
        # after parsing all training documents, calculate probabilities
        self.calcClassProbs()

    # parse a training document
    def parseTrainDoc(self, className, document):
        # if the class has not been observed before, create doctype
        # else increment the count and concatenate the doc to the text
        if className not in self.docTypes:
            self.docTypes[className] = DocumentType()
            self.docTypes[className].count = 1
            self.docTypes[className].text = document
        else:
            self.docTypes[className].count += 1
            self.docTypes[className].text += document
        # iterate over words in document
        for word in document:
            # build universal vocabulary of unique words by ignoring duplicates
            self.vocab.add(word)
            # count the number of times a word appears in the class
            if word not in self.docTypes[className].wordCounts:
                self.docTypes[className].wordCounts[word] = 1
            else:
                self.docTypes[className].wordCounts[word] += 1
        # increment the number of training documents
        self.numTrainDocs += 1

    # calculate probabilites for the classes
    def calcClassProbs(self):
        for className in self.docTypes:
            # estimate the probability for the particular class
            self.docTypes[className].prob = \
                float(self.docTypes[className].count) / float(self.numTrainDocs)
            # get the total number of word positions in the class text
            numWords = len(self.docTypes[className].text)
            # for each word in the vocabulary
            for word in self.vocab:
                # get the number of times a word occurs in the class text
                numWordCounts = 0
                if word in self.docTypes[className].wordCounts:
                    numWordCounts = self.docTypes[className].wordCounts[word]
                # estimate the probability of a word occurrence for doc type
                # using laplace smoothing
                self.docTypes[className].wordProbs[word] = \
                    float(numWordCounts + 1) / float (numWords + len(self.vocab))

    # classify unseen documents
    def classify(self, fileName):
        lines = self.parseFile(fileName, '\n\r', ' ')
        # since each line is a test document, parse it
        for line in lines:
            # the actual class name
            actualClass = line[0]
            # test document
            doc = line[1:]
            # classify the document using naive bayes
            cnb = self.naiveBayes(doc)
            # if classified matches actual class, then increment number correct
            if cnb == actualClass:
                self.numCorrect += 1
            # incrememnt number of test documents
            self.numTestDocs += 1
            # calculate the percent correct
            self.printScore(cnb, actualClass,
                            self.percentage(self.numCorrect, self.numTestDocs))

    # classify document using naive bayes classification
    # note: the "big product" is typically taken, but since probabilities are
    # very small (approaching zero), the summation of the logarithm of those
    # probabilities is taken in order to avoid architectural underflow
    def naiveBayes(self, document):
        # store probabilities for each possible class in dictionary
        classProbs = {}
        for className in self.docTypes:
            # get probability of class and convert to logarithm
            probSum = math.log(self.docTypes[className].prob)
            # for all word positions in document
            for word in document:
                # containing tokens in the vocabulary
                if word in self.vocab:
                    # probability of that word occurring given the document type
                    # and convert to logarithm before adding to summation
                    probSum += math.log(self.docTypes[className].wordProbs[word])
            # store the summation using the class name as the key
            classProbs[className] = probSum
        # find and return the maximum probability of all the classes
        return max(classProbs, key=classProbs.get)

    # find the percent correct out of a total
    def percentage(self, numCorrect, total):
        return (float(numCorrect) / float(total)) * 100.0

    # print score of classification since supervised learning
    def printScore(self, classified, actual, percentage):
        sys.stdout.write("Classified : {}\nActual : {}\nPercentage : {}%\n".format(classified, actual, percentage))
        sys.stdout.flush()

# parse commands from the command line for execution
def parseCommands():
    ArgParser = argparse.ArgumentParser()
    # add positional command line arguments expected to run program
    ArgParser.add_argument('trainingSet',
        help='The set of data to discover potentially predictive relationships.')
    ArgParser.add_argument("testSet",
        help='The set of data used to assess the strength and utility of a /\
              predictive relationship.')
    # parse the arguments passed to program and return as a dictionary where
    # key is the argument name, and value is the argument value passed
    return vars(ArgParser.parse_args())

# main driver of program
def main():
    dc = DocumentClassifier(parseCommands())
    dc.learn(dc.args['trainingSet'])
    dc.classify(dc.args['testSet'])

if __name__ == "__main__":
    main()

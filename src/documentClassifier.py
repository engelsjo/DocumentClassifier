"""
@summary: Implementation of Naive Bayes algorithm to determine what class (C)
a new document (D) belongs to.
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016
"""

import argparse
import math
import sys

# naive bayes document classifier
class DocumentClassifier(object):

    # constructor
    def __init__(self, args):
        # command line arguments for program execution
        self.args = args
        # set of unique words in training documentss
        self.vocab = set()
        # the number of training documents
        self.numTrainDocs = 0
        # dictionary of class names to document type objects
        self.docTypes = {}
        # track number of test documents classified
        self.numTestDocs = 0
        # track number classified correctly
        self.numCorrect = 0

    # learn how to classify a document
    def learn(self, fileName):

        # parse in data from file
        with open(fileName, 'rb') as fileHandler:
            for line in fileHandler:
                lineTokens = line.strip('\n\r').split(' ')
                # get class name
                className = lineTokens[0]
                # get document of words
                doc = lineTokens[1:]
                # if the class has not been observed before, create doctype
                # else increment the count and append the doc to the text
                if className not in self.docTypes:
                    self.docTypes[className] = DocumentType()
                    self.docTypes[className].count = 1
                    self.docTypes[className].text = doc
                else:
                    self.docTypes[className].count += 1
                    self.docTypes[className].text += doc
                # iterate over words in document
                for word in doc:
                    # build vocabulary of unique words by ignoring duplicates
                    self.vocab.add(word)
                    # count the number of times a word appears in the class
                    if word not in self.docTypes[className].wordCounts:
                        self.docTypes[className].wordCounts[word] = 1
                    else:
                        self.docTypes[className].wordCounts[word] += 1
                # incremement number of training docs
                self.numTrainDocs += 1

        # calculate probabilities for each class
        for className in self.docTypes:
            # estimate probability of a particular class
            self.docTypes[className].prob = float(self.docTypes[className].count) / float(self.numTrainDocs)
            # total number of word positions in text
            numWords = len(self.docTypes[className].text)
            # for each word in vocab
            for word in self.vocab:
                # number of times word occurs in text
                numWordCounts = 0
                if word in self.docTypes[className].wordCounts:
                    numWordCounts = self.docTypes[className].wordCounts[word]
                # calculate probability estimate of word occurrence for doc type
                # using laplace smoothing
                self.docTypes[className].wordProbs[word] = float(numWordCounts + 1) / float (numWords + len(self.vocab))

    # classify unseen documents
    def classify(self, fileName):

        # parse in data from file
        with open(fileName, 'rb') as fileHandler:
            for line in fileHandler:
                lineTokens = line.strip('\n\r').split(' ')
                # actual class name of test document
                actualClass = lineTokens[0]
                # get test document
                doc = lineTokens[1:]

                # store probabilities
                probs = {}
                # for all classes
                for className in self.docTypes:
                    # get probability of class
                    prob = math.log(self.docTypes[className].prob)
                    # for all word positions in document
                    for word in doc:
                        # containing tokens in vocab
                        if word in self.vocab:
                            # get the probability
                            # instead of big product, since values so small (underflow)
                            # use logarithmic addition (inverse of multiplication)
                            prob += math.log(self.docTypes[className].wordProbs[word])
                    probs[className] = prob
                # find the max probability
                cnb = max(probs, key=probs.get)
                # if classified matches actual class, then increment score
                if cnb == actualClass:
                    self.numCorrect += 1
                self.numTestDocs += 1
                self.percentCorrect = (float(self.numCorrect) / float(self.numTestDocs)) * 100.0
                sys.stdout.write("Classified: {}\nActual: {}\nPercentage: {}%\n".format(cnb, actualClass, self.percentCorrect))
                sys.stdout.flush()


# document type
class DocumentType(object):

    # constructor
    def __init__(self):
        # number of documents for which classification is this document type
        self.count = 0
        # probability estimate for this particular class (document type)
        self.prob = 0.0
        # single text for this type (concatenation of all documents for this type)
        self.text = []
        # dictionary of words in text to their counts for this document type
        self.wordCounts = {}
        # dictionary of words to probability estimates of word occurrence given
        # document type
        self.wordProbs = {}

def parseCommands():
    ArgParser = argparse.ArgumentParser()
    # add positional command line arguments expected to run program
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
    dc.classify(dc.args['testSet'])

if __name__ == "__main__":
    main()

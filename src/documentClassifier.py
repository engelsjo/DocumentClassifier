"""
@summary: Python script that classifies documents
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016
"""

import argparse

# http://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html

# naive bayes document classifier
class DocumentClassifier(object):

    def __init__(self, args):
        # command line arguments for program execution
        self.args = args
        # set of unique words in training documentss
        self.vocab = set()
        # the number of training documents
        self.numTrainDocs = 0
        # dictionary of class names to document type objects
        self.docTypes = {}

    def learn(self, fileName):
        # read file
        with open(fileName, 'rb') as fileHandler:
            # parse each line in file into tokens
            for line in fileHandler:
                # strip newline and return characters, split by space delimiter
                lineTokens = line.strip('\n\r').split(' ')
                # get class name (supervised learning)
                className = lineTokens[0]
                # get document of words
                doc = lineTokens[1:]
                # if the class has not been observed before initialize doctype
                # else increment the count and append the doc to the text
                if className not in self.docTypes:
                    self.docTypes[className] = DocumentType()
                    self.docTypes[className].count = 1
                    self.docTypes[className].text = doc
                else:
                    self.docTypes[className].count += 1
                    self.docTypes[className].text += doc
                # build vocabulary by adding each word to unique set of words
                for word in doc:
                    # only adds unique words to the vocab by ignoring duplicates
                    self.vocab.add(word)
                    # count the number of times a word appears in the class
                    if word not in self.docTypes[className].wordCounts:
                        self.docTypes[className].wordCounts[word] = 1
                    else:
                        self.docTypes[className].wordCounts[word] += 1
                # incremement number of training docs
                self.numTrainDocs += 1

        # for each class
        for className in self.docTypes:
            # estimate probability of a particular class
            classDocs = float(self.docTypes[className].count)
            trainDocs = float(self.numTrainDocs)
            self.docTypes[className].prob = classDocs / trainDocs
            # total number of word positions in textj
            n = len(self.docTypes[className].text)
            # for each word in vocab
            for word in self.vocab:
                # number of times wk occurs in textj
                nk = 0
                if word in self.docTypes[className].wordCounts:
                    nk = self.docTypes[className].wordCounts[word]
                # calculate probability estimate of word occurrence for doc type
                self.docTypes[className].wordProbs[word]

    def classify(self, fileName):
        x = 0

# document type
class DocumentType(object):

    def __init__(self):
        # number of documents for which classification is this document type
        self.count = 0
        # probability estimate for this particular class (document type)
        self.prob = 0.0
        # single text for this type (concatenation of all documents for this type)
        self.text = []
        # dictionary of words in text to their counts for this document type
        self.wordCounts = {}
        # probability estimate of word occurrence for this document type
        self.wordProbs = {}

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

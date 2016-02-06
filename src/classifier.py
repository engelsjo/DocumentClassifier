"""
@summary: Python script that classifies documents
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 3, 2016
"""

import sys
import pprint as pp
import numpy as np

train_dir = '../data/trainData/'
test_dir = '../data/testData/'

class Classifier(object):

    def __init__(self):
        self.table = {}
        self.vocab = {}
        self.classCount = {}
        self.vocab_table = {}
        self.prob_cj = {}
        self.nj = {}
        self.corpusSize = 0
        self.vocabSizeK = 0
        self.numClassesJ = 0
        self.prob_wkcj = np.array()

    def classify():
        print "hello from the other side"        

def main(argv):
    programName = argv[0]
    c = Classifier()
    dataFile = argv[1]
    if 'Train' in dataFile:
        dataFile = train_dir + dataFile
    else:
        dataFile = test_dir + dataFile
   	
    with open(dataFile, "r") as fh:
        for line in fh:
            lineParts = line.split(' ')

            # get the classes of docs
            docClass = lineParts[0]

            # get each doc corresponding to each class
            doc = lineParts[1:]

            # remove end line character from end word in doc
            doc[-1] = doc[-1].strip('\n')
            
            if (docClass not in c.table.keys()):
                # haven't seen class, so add to dict
                c.table[docClass] = doc
                # ???????
                c.vocab_table[docClass] = {}
                # first time seeing class
                c.classCount[docClass] = 1

            else:
                # append doc to master doc by class
                c.table[docClass] += doc
                # increment number of docs per class
                c.classCount[docClass] += 1

            for word in doc:
                # use dict for quick check if word
                #   has already appeared in dict
                c.vocab[word] = 0
               
                # if we have seen word, increment count
                try:
                    c.vocab_table[docClass][word] +=1 
                except Exception:
                    # we have not added a word yet
                    c.vocab_table[docClass][word] = 1
    
    # iterate over 20 classes to get corpusSize
    for cKey in c.classCount.keys():
        c.corpusSize += c.classCount[cKey]
    
    # probability estimate of a particular class
    for cKey in c.classCount.keys():
        count = float(c.classCount[cKey])
        size = float(c.corpusSize)
        c.prob_cj[cKey] = count / size 

    # total number of word positions in Text_j
    for cKey in c.table.keys():
        c.nj[cKey] = len(c.table[cKey])
   
    # get size of matrix
    vocabSizeK = len(c.vocab)
    amountClassesJ = len(c.classCount.keys())

    prob_wkcj = np.array([vocabSizeK,amountClassesJ])
        

if __name__ == "__main__":
    main(sys.argv)

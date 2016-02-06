"""
@summary: Python script that classifies documents
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 3, 2016
"""

import sys
import pprint as pp

train_dir = '../data/trainData/'
test_dir = '../data/testData/'

class Classifier(object):

    def __init__(self):
        self.table = {}
        self.vocab = {}
        self.classCount = {}
        self.vocab_table = {}

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
            docClass = lineParts[0]
            doc = lineParts[1:]
            doc[-1] = doc[-1].strip('\n')
            if (docClass not in c.table.keys()):
                c.table[docClass] = doc
                c.vocab_table[docClass] = {}
                c.classCount[docClass] = 1
            else:
                c.table[docClass] += doc
                c.classCount[docClass] += 1
            for word in doc:
                c.vocab[word] = 0
                try:
                    c.vocab_table[docClass][word] +=1 
                except Exception:
                    # we have not added a word yet
                    c.vocab_table[docClass][word] = 1
            #print "docClass: ", docClass
            #print "doc: ", doc
    #print c.table["baseball"]
    pp.pprint(c.classCount)
    print "len vocab:", len(c.vocab)
    #pp.pprint(c.vocab_table["baseball"])

    print len(c.table["baseball"])

if __name__ == "__main__":
    main(sys.argv)

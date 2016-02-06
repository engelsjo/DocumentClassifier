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
        self.vocab_table_with_probs = {}
        #self.prob_wkcj = np.array()

    def classify(self, aFile):
        # parse in the test data
        total_correct = 0
        total_docs = 0
        doc = []
        retVal = []
        with open(aFile, "r") as fh:
            for line in fh: # navigate through every file
                lineParts = line.split(' ')

                # get the classes of docs
                docClass = lineParts[0]

                # get each doc corresponding to each class
                doc = lineParts[1:]

                # remove end line character from end word in doc
                doc[-1] = doc[-1].strip('\n')

                all_probs = {}
                for a_class in self.vocab_table.keys():
                    curr_prob = self.prob_cj[a_class]
                    for word in doc:
                        if self.isInVocab(word):
                            curr_prob *= self.get_word_prob(a_class, word)
                    all_probs[a_class] = curr_prob

                #find the max for CNB
                CNB = max(all_probs, key=all_probs.get)
                retVal.append((docClass, CNB))
                if docClass == CNB:
                    total_correct += 1
                total_docs += 1
                percentage = (float(total_correct) / float(total_docs)) * 100.0

                sys.stdout.write("Intended : {}\nActual : {}\nPercentage : {}%\n".format(docClass, CNB, percentage))
                sys.stdout.flush()

        return retVal

    def isInVocab(self, aWord):
        try:
            word_val = self.vocab[aWord]
            return True
        except Exception:
            return False

    def generate_probs(self):
        # copy the structure of the self.vocab_table
        for a_class in self.vocab_table.keys():
            word_count_dict = self.vocab_table[a_class]

            #overwrite counts in self.vocab_table_with probs
            prob_wkcj = 0
            for word in word_count_dict.keys():
                try:
                    nk = word_count_dict[word]
                    prob_wkcj = float(nk + 1) / float(len(self.table[a_class]) + self.vocabSizeK)
                except KeyError:
                    # the word was not there
                    prob_wkcj = 1.0 / float(len(self.table[a_class]) + self.vocabSizeK)
                word_count_dict[word] = prob_wkcj
            self.vocab_table_with_probs[a_class] = word_count_dict

    def get_word_prob(self, aClass, aWord):
        word_probs_dict = self.vocab_table_with_probs[aClass]
        prob_wkcj = 0
        try:
            prob_wkcj = word_probs_dict[aWord]
        except Exception:
            # the word was not in word dict for this class, therefore we need to calc its probability
            prob_wkcj = 1.0 / float(len(self.table[aClass]) + self.vocabSizeK)

        return prob_wkcj
  

def main(argv):
    programName = argv[0]
    c = Classifier()
    dataFile = argv[1]
    testFile = ''
    if len(argv) == 3:
        testFile = argv[2]
        
    dataFile = train_dir + dataFile
    testFile = test_dir + testFile

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

    #prob_wkcj = np.array([vocabSizeK,amountClassesJ])

    # calc our probabilities
    c.generate_probs()

    intendedAndActual = c.classify(testFile)
    #pp.pprint(intendedAndActual)

        

if __name__ == "__main__":
    main(sys.argv)

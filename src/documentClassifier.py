"""
@summary: Implementation of Naive Bayes algorithm to classify documents.
@version: 1.0
@authors: Josh Engelsma, Adam Terwilliger, Michael Baldwin
@date: Febrary 11, 2016

References:
- http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/project2.pdf
- http://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html
- https://www.cs.cmu.edu/~schneide/tut5/node42.html
- http://stackoverflow.com/questions/16379313/how-to-use-the-a-10-fold-cross-validation-with-naive-bayes-classifier-and-nltk
"""

import argparse
import math
import progressbar

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
        # list of percentage corrects across k-trials
        self.percentCorrects = []

    # reset classifier
    def resetClassifier(self):
        self.numTrainDocs = 0
        self.numTestDocs = 0
        self.vocab = set()
        self.docTypes = dict()
        self.numCorrect = 0

    # print statistics on classifier effectiveness
    def printStats(self):
        print('Classifier Effectiveness:')
        print 'Correct: %d, Total: %d, Effectiveness: %d%%' % \
              (self.numCorrect, self.numTestDocs, \
               self.percentage(self.numCorrect, self.numTestDocs))

    # find the percent correct out of a total
    def percentage(self, numCorrect, total):
        return (float(numCorrect) / float(total)) * 100.0

    # print average effectiveness across k-trials
    def printAvgPercent(self, k):
        print 'Average Effectiveness across %d-trials: %d%%' % \
              (k, self.findAvg(self.percentCorrects))

    # find average of list of numbers
    def findAvg(self, listNums):
        return float(sum(listNums)) / float(len(listNums))

    # parse a file into a list of lists
    def parseFile(self, fileName, chars, delimiter):
        lines = []
        with open(fileName, 'rb') as fileHandler:
            for line in fileHandler:
                lineTokens = line.strip(chars).split(delimiter)
                lines.append(lineTokens)
        return lines

    # learn how to classify a document
    def learn(self, docList):
        # use progress bar to track computation time
        bar = progressbar.ProgressBar(max_value=len(docList)).start()
        print ('Learning from training documents:')
        # since each line is a training document, parse it
        for i in range(0, len(docList)):
            line = docList[i]
            className = line[0]
            doc = line[1:]
            self.parseTrainDoc(className, doc)
            # update progress bar
            bar.update(i)
        # finish progress bar
        bar.finish()
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
    def classify(self, docList):
        # use progress bar to track computation time
        bar = progressbar.ProgressBar(max_value=len(docList), \
                                      redirect_stdout=True).start()
        print ('Classifying test documents:')
        # since each line is a test document, parse it
        for i in range(0, len(docList)):
            line = docList[i]
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
            # display whether the classification was correct or not
            # print 'Classified: %s, Actual: %s' % (cnb, actualClass)
            # update the progress bar
            bar.update(i)
        # finish progress bar
        bar.finish()

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

    # k-fold cross validation where k is the number of iterations
    # average error is computed across all k trials
    def kFold(self, fileName, k):
        print 'Naive bayes classification with %d-fold cross validation:' % (k)
        # parse the dataset into a list of lists
        lines = self.parseFile(fileName, '\n\r', ' ')
        # calculate the offset based on the number of documents and k
        offset = len(lines) / k
        # for each fold, learn and classify
        for i in range(0, k):
            # test set starts at the iteration times the offset,
            # then splice again up until offset - 1
            testSet = lines[i * offset:][:offset]
            # training set starts at begining up until iteration times offset
            # (if offset is zero then this is empty), then append the rest
            # from iteration plus 1 times offset until end
            trainSet = lines[:i * offset] + lines[(i + 1) * offset:]
            # learn
            self.learn(trainSet)
            # classify unseen documents
            self.classify(testSet)
            # print current statistics of classifier
            self.printStats()
            # update the average percent effectiveness (percent correct)
            self.percentCorrects.append( \
                            self.percentage(self.numCorrect, self.numTestDocs))
            # reset classifier for next iteration
            self.resetClassifier()
        # print average effectiveness (percent correct)
        self.printAvgPercent(k)


# parse commands from the command line for execution
def parseCommands():
    ArgParser = argparse.ArgumentParser()
    # add positional command line arguments expected to run program
    ArgParser.add_argument('dataSet',
        help='The set of data to perform k-fold cross validation on.')
    ArgParser.add_argument('k', help="The number of folds to run trials.")
    # parse the arguments passed to program and return as a dictionary where
    # key is the argument name, and value is the argument value passed
    return vars(ArgParser.parse_args())

# main driver of program
def main():
    dc = DocumentClassifier(parseCommands())
    dc.kFold(dc.args['dataSet'], int(dc.args['k']))

if __name__ == "__main__":
    main()

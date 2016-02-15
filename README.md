# DocumentClassifier (CIS 678 - Project 2)

## Authors
Michael Baldwin, Joshua Engelsma, Adam Terwilliger

## Objective
Document Classification using the Naive Bayes Algorithm

## Specification
The basic idea is to write a program that, given a collection of training data consisting
of category-labeled documents, “learns” how to classify new documents into the
correct category using a Naïve Bayes classifier.

## Background
The Naïve Bayes algorithm uses probabilities to perform classification. The
probabilities are estimated based on training data for which the value of the
classification is known (i.e. it is another form of Supervised Learning). The
algorithm is called “naïve” because it makes the simplifying assumption that
attribute values are completely independent, given the classification.

## Usage
### Install Progress Bar
```
sudo pip install progressbar2
```
### Holdout Method
```
python src/documentClassifier.py holdout data/trainData/forumTraining.data data/testData/forumTest.data
```
### K-Fold Cross Validation
```
python src/documentClassifier.py kfold data/mergedData/forum.data k
```
### Random Subsampling
```
python src/documentClassifier.py random data/mergedData/forum.data k s
```
### Automate N K-Fold Trials
```
bash src/kfoldAutomate.sh n
```
### Word Cloud Visualization by Class
```
python src/wordcloudPreprocess.py data/mergedData/forum.data
http://www.wordle.net/create
```

## TO-DO
### Required
- Design Doc
- Visualization of k-fold results

### Extra  
- Positivity/Negativity rating for politicians/scientists
- N grams (uni-grams, bi-grams, tri-grams)
- Maximum entropy classifier

## Other Ideas  
#### Word frequency (lists of words and their frequencies)  
#### Collocation (words commonly appearing near each other)   
#### Concordance (the contexts of a given word or set of words)  
#### N-grams (common two-, three-, etc.- word phrases)  
#### Entity recognition (identifying names, places, time periods, etc.)  
#### Dictionary tagging (locating a specific set of words in the texts)  
#### [Word Cloud Visualization](https://github.com/jasondavies/d3-cloud)

## High-level Goals for Text Analysis  
- Document categorization  
- Information retrieval (e.g., search engines)  
- Supervised classification (e.g., guessing genres)  
- Unsupervised clustering (e.g., alternative “genres”)  
- Corpora comparison (e.g., political speeches)  
- Language use over time (e.g., Google ngram viewer)  
- Detecting clusters of document features (i.e., topic modeling)   
- Entity recognition/extraction (e.g., geoparsing)  
- Visualization   

## Helpful Links
- [Simple Explanation of Naive Bayes](http://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification)   
- [Where to start with text mining](http://tedunderwood.com/2012/08/14/where-to-start-with-text-mining/)   
- [Intro to Topic Modeling](http://journalofdigitalhumanities.org/2-1/topic-modeling-a-basic-introduction-by-megan-r-brett/)
- [Naive Bayes Time Complexity](http://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html)
- [K-fold Cross Validation](https://www.cs.cmu.edu/~schneide/tut5/node42.html)
- [Python - Time Complexity of Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
- [Python Progress Bar](https://github.com/WoLpH/python-progressbar)
- [Python K-fold Cross Validation](http://stackoverflow.com/questions/16379313/how-to-use-the-a-10-fold-cross-validation-with-naive-bayes-classifier-and-nltk)

## Project Info
### Dataset
- [Project Info](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/project2.pdf)
- [Training Dataset](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTraining.data)
- [Test Dataset](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTest.data)
- [Training Dataset w/stemming](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTraining-stemmed.data)
- [Test Dataset w/stemming](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTest-stemmed.data)
- kfold dataset creation:
```
mkdir kfoldData
cp trainData/forumTraining.data kfoldData/
cp testData/forumTest.data kfoldData/
cat kfoldData/forumTest.data >> kfoldData/forumTraining.data
rm kfoldData/forumTest.data
mv kfoldData/forumTraining.data kfoldData/forum.data
```

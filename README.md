# DocumentClassifier
## CIS 678 - Project 1

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

## TO-DO
### Required
- Alternative/additional data pre-processing  
- k-fold cross validation  


## Other Ideas  
#### Word frequency (lists of words and their frequencies)  
#### Collocation (words commonly appearing near each other)   
#### Concordance (the contexts of a given word or set of words)  
#### N-grams (common two-, three-, etc.- word phrases)  
#### Entity recognition (identifying names, places, time periods, etc.)  
#### Dictionary tagging (locating a specific set of words in the texts)  

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

## Project Info
### Dataset
- [Project Info](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/project2.pdf)
- [Training Dataset](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTraining.data)
- [Test Dataset](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTest.data)
- [Training Dataset w/stemming](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTraining-stemmed.data)
- [Test Dataset w/stemming](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTest-stemmed.data)

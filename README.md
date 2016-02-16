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

## TO-DO
### Required
- Design Doc
- Run random for k-fold percents (50/50, 40/60, 30/60, 20/80, ...)
- Visualization of validation results

### Extra  
- Positivity/Negativity rating for politicians/scientists
- N grams (uni-grams, bi-grams, tri-grams)
- Maximum entropy classifier

## Project Info
### Dataset
- [Project Info](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/project2.pdf)
- [Training Dataset](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTraining.data)
- [Test Dataset](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTest.data)
- [Training Dataset w/stemming](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTraining-stemmed.data)
- [Test Dataset w/stemming](http://www.cis.gvsu.edu/~wolffe/courses/cs678/projects/forumTest-stemmed.data)

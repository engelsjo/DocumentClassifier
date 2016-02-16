# DocumentClassifier (CIS 678 - Project 2)

## Authors
Michael Baldwin, Joshua Engelsma, Adam Terwilliger

## Objective
Document Classification using the Naive Bayes Algorithm

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
### Automate N Random Trials with Various Sizes
```
bash src/randomAutomate.sh n firstSize lastSize step
```
### Word Cloud Visualization by Class
```
python src/wordcloudPreprocess.py data/mergedData/forum.data
http://www.wordle.net/create
```
### Kfold dataset creation:
```
mkdir kfoldData
cp trainData/forumTraining.data kfoldData/
cp testData/forumTest.data kfoldData/
cat kfoldData/forumTest.data >> kfoldData/forumTraining.data
rm kfoldData/forumTest.data
mv kfoldData/forumTraining.data kfoldData/forum.data
```

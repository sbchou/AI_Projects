Sophie Chou
sbc2125
May 2013

COMS 4701 Artificial Intelligence HW4

* Programming Language: python
* Python Version 2.7.1

Implements the ID3 tree learning algorithm to output a Decision Tree script to classify data.
http://en.wikipedia.org/wiki/ID3\_algorithm

Files:

* README.md
* restaurant\_training.csv, the training data
* restaurant\_test.csv, the testing data
* tree\_learner.py, which will generate:
* classifier.py

TO RUN: 

* to run the tree-learning algorithm, type the command:
* python tree\_learner.py restaurant\_training.csv 
* This creates a classifying script using your generated tree in the file classifier.py.

* To run the classifier on the given test data, run:
* python classifier.py restaurant\_test.csv

* This will output the classifications to the screen.

TEST RESULTS:

* For restaurant\_test.csv we get the following classifications:
* Yes
* No
* Maybe

REFERENCES

http://en.wikipedia.org/wiki/ID3\_algorithm

http://www.onlamp.com/pub/a/python/2006/02/09/ai\_decision\_trees.html


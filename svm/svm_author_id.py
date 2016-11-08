#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from datetime import datetime
sys.path.append("../tools/")
sys.path.append("../choose_your_own/")

from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

def timeit(func):
    t1 = datetime.now()
    res = func()
    t2 = datetime.now()
    return res, (t2-t1).total_seconds()


features_train, features_test, labels_train, labels_test = preprocess()



def predictfunc(classifier, length):
    _, training_time_used = timeit(lambda :classifier.fit(features_train[:length], labels_train[:length]))
    predicted, predit_time_used = timeit(lambda: classifier.predict(features_test))

    print accuracy_score(labels_test, predicted)
    return predicted


clf = SVC(kernel="linear", gamma=1.0)
clf_rbf = SVC(kernel="rbf", gamma=1.0)

clf_rbf_c1 = SVC(kernel="rbf", C=10)
clf_rbf_c2 = SVC(kernel="rbf", C=100)
clf_rbf_c3 = SVC(kernel="rbf", C=1000)

clf_rbf_c4 = SVC(kernel="rbf", C=10000)

# print predictfunc(clf, length=len(features_train)/100)

# print predictfunc(clf_rbf_c1, length=len(features_train)/50)
# print predictfunc(clf_rbf_c2, length=len(features_train)/50)
# print predictfunc(clf_rbf_c3, length=len(features_train)/50)
# print predictfunc(clf_rbf_c4, length=len(features_train)/50)

# res = predictfunc(clf_rbf_c4, length=len(features_train)/100)
res = predictfunc(clf_rbf_c4, length=len(features_train))
print len(filter(lambda r: r == 1, res))

# console.log(items.filter(function(item) { return item == 1 }).length)




#########################################################
### your code goes here ###

#########################################################



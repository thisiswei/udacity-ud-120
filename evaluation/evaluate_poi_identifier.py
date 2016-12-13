#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
clf = DecisionTreeClassifier()


from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
print accuracy_score(labels_test, pred)

print len([p for p in pred if p == 1])
print len(pred)


indexes = [i for (i, x) in enumerate(labels_test) if x == 1]
print len(filter(lambda p: p == 1, [pred[i] for i in indexes]))



from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


print 'precision', precision_score(labels_test, pred)
print 'recall', recall_score(labels_test, pred)


predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]


# precision = tp / (tp + fp)
# 6 / 9

# recall = tp / (tp + fn)
# 6 / (6+2)

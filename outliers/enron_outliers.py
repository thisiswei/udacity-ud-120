#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( 'TOTAL' )
features = ["salary", "bonus"]

keys = sorted(data_dict.keys())
data = featureFormat(data_dict, features, sort_keys=keys)
import ipdb; ipdb.set_trace()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()


### your code below
salaries = []
bonuses = []

for point in data:
    salary = point[0]
    bonus = point[1]
    salaries.append(salary)
    bonuses.append(bonus)

    matplotlib.pyplot.scatter( salary, bonus )


def _clean(pairs):
    length  = int(len(pairs) * 0.7)
    pairs = sorted(pairs, key=lambda p: p[1])[:length]
    return zip(*pairs)



clean_salaries, clean_bonuses = _clean(zip(salaries, bonuses))



import numpy

clean_salaries = list(clean_salaries)
clean_bonuses = list(clean_bonuses)
clean_salaries = numpy.reshape( numpy.array(clean_salaries), (len(clean_salaries), 1))

clean_bonuses = numpy.reshape( numpy.array(clean_bonuses), (len(clean_bonuses), 1))
salaries = numpy.reshape( numpy.array(salaries), (len(salaries), 1))

reg.fit(clean_salaries, clean_bonuses)
predicted_bonuses = reg.predict(salaries)
outliner = sorted(
    [
        (i, actual_bonus, predict_bonus*predict_bonus - actual_bonus*actual_bonus)
        for (i, (predict_bonus, actual_bonus)) in enumerate(zip(predicted_bonuses, bonuses))
    ],
    key=lambda c: c[-1],
)


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

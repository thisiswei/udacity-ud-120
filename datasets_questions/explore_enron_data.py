#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

keys = enron_data.keys()

print len(filter(lambda key: enron_data[key]['poi'] == True, keys))

# keys.filter()
# fitler(, keys)

james_keys = filter(lambda key: key[:len('PRENTICE JAMES')] == 'PRENTICE JAMES', keys)

print james_keys
total_stock_by_james = reduce(lambda acc, key: acc + enron_data[key]['total_stock_value'], james_keys, 0)
print total_stock_by_james

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# catch_names = function(name) {
#     return enron_data.keys().filter(function(key) {
#         return key[: len(name)] == name;
#     }
# };

def catch_names(name):
    return filter(lambda key: key[:len(name)] == name, enron_data.keys())

names = catch_names('SKILLING JEFFREY')

# names.reduce(function(name, acc) {
#     const stock_options = enron_data[name]['exercised_stock_options'];
#     if(stock_options == 'Nah') {
#             return acc;
#     }
#     return acc + stock_options;
# }, 0);

def _func(acc, name):
    stock_options = enron_data[name]['exercised_stock_options'];
    return acc+stock_options if stock_options is not 'NaN' else acc


print reduce(_func, names, 0)

# Lay, Skilling and Fastow
print catch_names('LAY')
print catch_names('SKILLING')
print catch_names('FASTOW')

# const get_feature= function(names, feature) {
#     return names.reduce(function(name, acc) {
#         const _feature = enron_data[name][feature];
#         if(_feature == 'NaN') {
#                 return acc;
#         }
#         return acc+ _feature;
#     }, 0)
# };

def get_feature(names, feature):
    def _func(acc, name):
        _feature = enron_data[name][feature];
        return acc + _feature if _feature != 'NaN' else acc

    return reduce(_func, names, 0)

def get_total_payments(names):
    return get_feature(names, 'total_payments')

print get_total_payments(catch_names('LAY'))
print get_total_payments(catch_names('SKILLING'))
print get_total_payments(catch_names('FASTOW'))

print len(filter(lambda key: enron_data[key]['salary'] != 'NaN', keys))
print len(filter(lambda key: enron_data[key]['email_address'] != 'NaN', keys))

print len(filter(lambda key: enron_data[key]['total_payments'] == 'NaN', keys))
print len(keys)
print 21/146.

pois = filter(lambda key: enron_data[key]['poi'] == True, keys)

print len(filter(lambda key: enron_data[key]['total_payments'] == 'NaN', pois))
print len(pois)
print '\n'
print len(keys)
print len(filter(lambda key: enron_data[key]['total_payments'] == 'NaN', keys))

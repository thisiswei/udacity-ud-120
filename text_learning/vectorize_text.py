#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 1000000:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            ps = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            nameStr =  ["sara", "shackleton", "chris", "germani"]
            text = reduce(lambda acc, elem: acc.replace(elem, ''), nameStr, ps)
            ### append the text to word_data
            word_data.append(text)

            if name == 'sara':
                from_data.append(0)
            else:
                from_data.append(1)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris


            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )




from nltk.corpus import stopwords
def _remove_stop_words(text):
    sw = stopwords.words('english')
    return reduce(lambda acc, elem: acc.replace(elem, ''), sw, text)

    # return sw.reduce(function(acc, elem) {
    #     return acc.replace(elem, "" )
    # }, text)


### in Part 4, do TfIdf vectorization here
print word_data[152]
# from sklearn.feature_extraction.text import TfidfTransformer
# transformer = TfidfTransformer()
# transformer.fit(word_data)

# print transformer.get_feature_names()


from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
tf.fit(_remove_stop_words(' '.join(word_data)).split())
print len(tf.get_feature_names())

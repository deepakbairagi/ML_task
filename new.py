import numpy as np
import pandas as pd
# This is for apple and origin 
# Smooth is for apple and bumpy is for orange
features = [[100,0],[120,0],[130,1],[150,1]]
# 0 equal smooth and 1 equal bumpy
# Now answers accordingly
label = ["apple",'apple','orange','orange']
# order of label should be similar to features
from sklearn.tree import DecisionTreeClassifier
# Calling Decision Tree Classifier
clf = DecisionTreeClassifier()
# Now Time for Training Data
trained=clf.fit(features,label)
#  The is need to be always in numerical format

# Now Prediciting
trained.predict([[123,1]])

array(['orange'], dtype='<U6')


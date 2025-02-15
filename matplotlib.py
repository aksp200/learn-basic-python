# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:23:47 2025

@author: akshay
"""

import matplotlib.pyplot as plot
import pandas as pd
from sklearn import datasets


iris = datasets.load_iris()
x=iris.data
y=iris.target

x_labels = iris.feature_names

df= pd.DataFrame(x,columns=x_labels)
print(df.head())

plot.plot(df[df.columns[0]])

plot.scatter(df[df.columns[0]],df[df.columns[1]])

plot.scatter(df[df.columns[0]],df[df.columns[1]], c=iris.target)

plot.hist2d(df[df.columns[0]], df[df.columns[1]])
plot.legend()
plot.show()
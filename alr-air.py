import altair as alt
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
x = iris.data
y = iris.target
x_labels = iris.feature_names
df = pd.DataFrame(x,columns=x_labels)
df["species"]= [iris.target_names[p] for p in y]
print(df.head())


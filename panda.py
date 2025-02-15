import pandas as pd
import numpy as np

a = np.random.rand(150,4)
print(a)
a_labels = ["sepal length(cm)","sepal width(cm)","petal length(cm)","petal width(cm)"]
np.shape(a_labels)
df = pd.DataFrame(data=a, columns=a_labels)
print("first 2 elements")
df.head(2)

print("last 3 elements")
df.tail(3)

print(df["sepal length(cm)"].size)

print(df.index%2==0)


``

print(df[df["sepal length(cm)"]<.3].size)




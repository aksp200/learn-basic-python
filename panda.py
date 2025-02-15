import pandas as pd
import numpy as np

a = np.random.rand(150,4)

print(a)
a_labels = ["a","b","c","d"]
np.shape(a_labels)
df = pd.DataFrame(data=a, columns=a_labels)
print("first 2 elements")
df.head(2)

print("last 3 elements")
df.tail(3)

print(df["a"].size)

print(df.index)


lessThanDf= df[df["a"]<.3]

print(lessThanDf)

oddDf=df[df.index%2!=0]
print(oddDf)

print(df.describe())

transposeDf = df.T

print(transposeDf)

print(transposeDf.describe())

print(df.sort_values(by="a").describe())
 
print("add a col in df")

df["e"]  = np.random.rand(150)

df["f"] = np.random.randint(1,5,150)

print(df.groupby(by="f").count())

print(df.fillna(0.00000000001).head())

print(df.groupby(by="f").count())




#sdcp = pd.read_csv("data/sleep_deprivation_dataset_detailed.csv")

sdcp = pd.read_csv(r"C:\Users\akshay\git\learn-basic-python\data\sleep_deprivation_dataset_detailed.csv")
print(sdcp.describe())

sdcp.groupby(by="Sleep_Quality_Score")
quality_score_bins = [0,20,40,60,80,100]
quality_score_bin_labels = ["0-20","20-40","40-60","60-80","80-100"]

sleep_hours_bins = [0,2,4,6,8,10]
sleep_hours_bins_labels = ["0-2","2-4","4-6","6-8","8-10"]


sdcp["Sleep_Quality_Score_Range"]=pd.cut(sdcp["Sleep_Quality_Score"],bins=quality_score_bins,labels=quality_score_bin_labels)
sdcp["Sleep_Hours_Range"]=pd.cut(sdcp["Sleep_Hours"],bins=sleep_hours_bins,labels=sleep_hours_bins_labels)

print(sdcp["Sleep_Hours_Range"])

print(sdcp["Sleep_Hours","Sleep_Quality_Score","Sleep_Hours_Range"].head(3))

sdcp.to_json(r"C:\Users\akshay\git\learn-basic-python\data\sleep_deprivation_dataset_detailed.json", orient="records",indent=4)





# Download latest version
df = pd.read_csv(r"C:\Users\akshay\git\learn-basic-python\data\cars93.csv")

print("car93 df:", df)
print("car93 df:", df.columns)


print("\n drop rows with NaN")
print(df.describe())
print(df.dropna().describe())


print("\n drop rows with NaN threshold of more than 1 NaN values")
print(df.describe())
print(df.dropna(thresh=1).describe())

print("\n fill NaN")
print(df.describe())
#df.fillna("----Ignore----").to_csv(r"C:\Users\akshay\git\learn-basic-python\data\cars93_cleaned.csv")

print("replace with local average")
print(df.columns)
mask = df[["Rear.seat.room","Luggage.room"]].rolling(3,center=True,min_periods=1).mean()
#mask = df['Rear.seat.room', 'Luggage.room'].rolling(3,center=True,min_periods=1).mean()
df[df[['Rear.seat.room', 'Luggage.room']].isnull()]=mask
df.to_csv(r"C:\Users\akshay\git\learn-basic-python\data\cars93_cleaned_local_mean.csv")





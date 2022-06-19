""" A DATA FRAME A TABULAR DATASTRUCTURE OR A COLLECTION OF SERIES """
import pandas as pd

df = pd.DataFrame(['DL', 'UP', 'AP', 'TS'])
print(df)
print(df[0][0])
act=[100,200,300,400]
df[1]=act
print(df)
df.columns=['Cities','Active' ]
print(df)
NewInd = df.set_index('Cities',inplace=True)
print(NewInd)




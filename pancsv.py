import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/SUDHANSU/Desktop/AAAPYTHONYOUNIS/DATASETFILES/student_data1.csv')
print(df.head(),"gives 5 entries default")
print()
print(df.tail(3),"gives the last 10 from the last of the dataset")
print()
print(df.shape,"gives the  column and rows")
print()
print(df.shape[1],"gives the  column ")
print()
print(df.columns,"gives only column")
print()
print(df.dtypes)
print(df.student_id,"to give column of the particular id")
print()
print(df.describe())
print()
print(df.marks.min(),'gives the minm value')
print()


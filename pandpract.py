import pandas as pd
from array import *

# z = pd.Series('d', [1, 2, 3, 4])
# print(z)

# data = pd.Series([1, 2, 3, 4], index=['DL', 'UP', 'AP', 'TS'], dtype='int64')
# print(data)
# print("index can be changed", "data type can be changed")
# print(data[0])
# print(data.dtype)
# print(data.ndim)
# print(data.shape)
# print(data[['DL', 'AP']])
# print(data[data >= 2])
# print(data[::-1])
#
#
# x1 = pd.Series([1, 2,3,4,5])
# y1 = pd.Series([12,24,56,78])
# print(x1+y1)
# print(y1-x1)
# print(y1/x1)
# print(x1.max())
# print(x1.mean())
# print(x1.std())
# tarr = pd.DataFrame([1,2,3,4],[5,6,7,8])
# print(tarr)

d ={'Name':['Alisa','Bobby','Catherine','Madonna','Rockey','Sebastian'],'Score1':[56,85,23,48,64,78],'Score2':[56,39,43,61,89,94]}

def adder(x,y):
    return(x+y)

print(df['Score1'].pipe(adder,2))


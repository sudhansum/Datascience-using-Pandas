import numpy as np
from array import *
import pandas as pd
import sys
d = np.array([1, 2, 3, 4, 5])
print(d, type(d))
d = d+2
print(d , "can perform vector operations")


x = pd.Series([1,2,3,4,5])
print(x,type(x))


# lst = list(range(1,100001))
# narr = np.arange(1,100001)
# print(sys.getsizeof(1)*len(lst))
# print(narr.size*narr.itemsize)
#
# import time
# s = 10000000
# x1= list(range(s))
# x2= list(range(s))
# start=time.time()
# r1=[x+y for x,y in zip(x1,x2)]
# end = time.time()
# print((end - start)*1000)
#
# y1=np.arange(s)
# y2=np.arange(s)
# start=time.time()
# r2 = y1+y2
# end = time.time()
# print((end - start)*1000)

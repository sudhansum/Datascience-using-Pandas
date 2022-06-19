import numpy as np

 '''13TH DECEMBER'''
a = np.array([1, 2, 3, 4, 5])
print(a.shape)
print(a.ndim)
print(a.dtype)


b=np.array([[1, 2, 3],[ 4, 5,6],[7,8,9]])
print(b.shape)
print(b.ndim)
print(b.dtype)
#
# z = np.zeros((10,10))
# print(z)
#
# onm = np.ones((5,5))
# print(onm)
#
#
# I = np.eye(4,4)
# print(I)
# print(I.flatten())
# #print(I.reshape())
#
#
# ary = np.arange(1,26).reshape(5,5)
# print(ary)
# print(ary[0],"gives rows")
# print(ary[2:,], "row slicing")
# print(ary[:,3])
# print(ary[:,1:3], " i want 1 and 2 column")
# print(ary[:,[1,3,4]],"I want 1,2,3 colums and all the row")
# print(ary[2,1:4],"2nd row and 1,2,3 columns")
# print(ary[1:,4])
# print(ary[1:4,0:3])
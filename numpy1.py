# importing numpy module for numpy array
import numpy as np
rows=int(input("enter no of rows"))
col=int(input("enter no of columns"))
l=rows*col
a=np.random.randint(low=1,high=100,size=l).reshape((rows,col))
a 
np.save('arrfile',a)
print("the array is saved in the arrfile.npy!!")

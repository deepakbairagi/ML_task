import numpy as np
r=int(input("enter no of rows"))
c=int(input("enter no of columns"))
l=r*c
a=np.random.randint(low=1,high=100,size=l).reshape((r,c))
a
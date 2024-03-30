import numpy as np
#create the matrix
A = np.array([[1,2,3,4],[-2,4,-3,5],[-1,3,-3,4]])
print('A = ')
print(A)
#access the second row, third column
a23 = A[1,2]
print('The value in the second row, third column is ',a23)
#find the size of the matrix
m,n = np.shape(A)
print('rows = {}. cols = {}'.format(m,n))
#get the third row of the matrix
Arow3 = A[2,:]
print('The third row is ',Arow3)
#get the second column of the matrix
Acol2 = A[:,1]
print('The second column is ',Acol2)


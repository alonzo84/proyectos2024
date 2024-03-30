import numpy as np
#create the matrix
A = [[1,-3,2,-1],[2,-4,5,2],[-1,3,-1,3],[3,2,-1,-1]]
B = [[6],[13],[-23],[6]]
solucion = np.linalg.solve(A,B)

print(solucion)

print('x={:.2f}. y = {:.2f}, z = {:.2f}, w = {:.2f}'.format(solucion[0,0], solucion[1,0], solucion[2,0], solucion[3,0]))

# print('A = ')
# print(A)
# #access the second row, third column
# a23 = A[1,2]
# print('The value in the second row, third column is ',a23)
# #find the size of the matrix
# m,n = np.shape(A)
# print('rows = {}. cols = {}'.format(m,n))
# #get the third row of the matrix
# Arow3 = A[2,:]
# print('The third row is ',Arow3)
# #get the second column of the matrix
# Acol2 = A[:,1]
# print('The second column is ',Acol2)


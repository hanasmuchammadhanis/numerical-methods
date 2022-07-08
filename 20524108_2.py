#Gauss
import numpy as np
import sys
n = int(input('Masukkan angka yang belum diketahui: '))
a = np.zeros((n,n+1))
x = np.zeros(n)
print('Masukkan koefisien matriks:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Bagi 0!')
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
x[n-1] = a[n-1][n]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]
print('\nSolusi harapan: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')

#Gauss Jordan
import numpy as np
import sys
n = int(input('Masukkan angka yang belum diketahui: '))
a = np.zeros((n,n+1))
x = np.zeros(n)
print('Masukkan koefisien matriks:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Bagi 0!')
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
for i in range(n):
    x[i] = a[i][n]/a[i][i]
print('\nSolusi harapan: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')

#LU
A = [[1, -4, 2, 3],
     [2, 1, 3, -1],
     [4, 1, 2, -3],
     [3, -4, -2, 2]]
B = [2, 0, 1, 8]
def show(matrix):
    n = len(matrix)
    for row in range(n):
      for col in range(n):
        print('%.2f' % matrix[row][col], end="\t")
      print("")
show(A)
n = len(A)
L = [[0 for row in range(n)]
   for col in range(n)]
U = [[0 for row in range(n)]
   for col in range(n)]
for p in range(n):
  for j in range(p,n):
    sum = 0
    for k in range(p):
      sum = sum + L[p][k]*U[k][j]
    U[p][j] = A[p][j] - sum
q = p
for i in range (q,n):
  if (i==q):
    L[i][q]=1
  else:
    sum = 0
    for k in range(q):
      sum = sum + L[i][k]*U[k][q]
    L[i][q] = (A[i][q] - sum)/U[q][q]

def decomposition(A):
  n = len(A)
  L = [[0 for row in range(n)]
       for col in range(n)]
  U = [[0 for row in range(n)]
       for col in range(n)]
  for p in range(n):
    for j in range(p,n):
      sum = 0
      for k in range(p):
        sum = sum + L[p][k]*U[k][j]
      U[p][j] = A[p][j] - sum
    q = p
    for i in range (q,n):
      if (i==q):
        L[i][q]=1
      else:
        sum = 0
        for k in range(q):
          sum = sum + L[i][k]*U[k][q]
        L[i][q] = (A[i][q] - sum)/U[q][q]
  return L, U
A = [[1, -4, 2, 3],
     [2, 1, 3, -1],
     [4, 1, 2, -3],
     [3, -4, -2, 2]]
L, U = decomposition(A)
print("Matrix L :")
show(L)
print("\nMatrix U :")
show(U)
def forward_subs(B,L):
  n = len(B)
  t = [[0 for row in range(n)]
      for col in range(n)]
  for i in range(n):
    sum = 0
    for j in range(i):
      sum = sum + L[i][j]*t[j] 
    t[i] = B[i] - sum
  return t
def backward_subs(t,U):
  n = len(t)
  x = [[0 for row in range(n)]
      for col in range(n)]
  for i in range(n,0,-1):
    sum = 0
    for j in range(i,n):
      sum = sum + U[i-1][j]*x[j]  
    x[i-1] = (1/U[i-1][i-1])*(t[i-1]-sum)
  return x
def solve_LU(A,B):
  n   = len(A)
  L,U = decomposition(A)
  t   = forward_subs(B,L)
  x   = backward_subs(t,U)
  return x
A = [[1, -4, 2, 3],
     [2, 1, 3, -1],
     [4, 1, 2, -3],
     [3, -4, -2, 2]]
B = [2, 0, 1, 8]
x = solve_LU(A,B)
for i in range(len(x)):
  print('x_%d : %.2f' %(i+1,x[i]))

#Invers
import numpy as np
import sys 
A = np.array([[1, -4, 2, 3],
              [2, 1, 3, -1],
              [4, 1, 2, -3],
              [3, -4, -2, 2]])
print(np.linalg.inv(A))
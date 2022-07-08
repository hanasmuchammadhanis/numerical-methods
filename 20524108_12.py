#euler
def f (x):
  return - 2*x**3 + 12*x**2 - 20*x + 8.5
h  = 0.5
n  = int(10/h)
x  = 0
y  = 1
for i in range (1,n+1):
  k = f (x)
  y = y + h*k
  x = x + h
  print (i,'\tx =',x,'\ty =',y)
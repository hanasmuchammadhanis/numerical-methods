#integrasi
def f (x):
  return 5 - 2*x  + 4*x**2 - 1*x**3 - 8*x**5
n = int (input('n = '))
h = 0.8/n
k = 0
for i in range (1,n):
  c = i*h
  k = k + 2*f(c)
k = (h/2)*(f(0) + k + f(0.8))
E = abs((k-3.59)/3.59)*100
print('Nilai analitik = 3.59')
print('Nilai numerik  = ',k)
print('Error          = ',abs((k-3.59)/3.59)*100,'%')
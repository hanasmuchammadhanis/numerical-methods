#simpson
def f1 (a, b, c, d, n):
  def f2 (x):
    return 5 - 10*x  + 15*x**2 - 20*x**3 + 25*x**4 - 30*x**5
  h  = (0.8 - a)/n
  y  = f2 (a)
  y1 = 0
  y2 = 0
  for i in range (1, n):
    xi = a + i*h
    if i % b == 0:
       y1 =  y1 + f2 (xi)
    else :
       y2 =  y2 + f2 (xi)
  y         = y + c*y1 + d*y2 + f2 (0.8)
  simpson   = (1/3)*h*y
  return simpson
print('Simpson 1/3')
print('Nilai analitik =  1.64')
print('Nilai numerik  = ', f1 (0, 2, 2, 4, 8))
print('Error          = ', abs((f1 (0, 2, 2, 4, 8)-1.64)/1.64)*100,'%')
print('\nSimpson 3/8')
print('Nilai analitik =  1.78752')
print('Nilai numerik  = ', f1 (0.2, 3, 2, 3, 3))
print('Error          = ', abs((f1 (0.2, 3, 2, 3, 3)-1.78752)/1.78752)*100,'%')
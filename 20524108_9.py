#lagrange
import numpy 
import math
n = int(input('Jumlah data = '))
x = numpy.zeros((n))
y = numpy.zeros((n))
for i in range(n):
    x[i] = float(input( 'x['+str(i)+'] = '))
    y[i] = float(input( 'y['+str(i)+'] = '))
xp = int(input('Nilai yang diinterpolasi = '))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]    
et = (((yp-math.log10(xp))/(math.log10(xp)))*100)*(-1)
print('Nilai interpolasi',xp, '=' ,yp)
print('Error =', et,'persen')

        

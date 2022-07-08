#Regresi
import pandas as pa
data = pa.read_csv('/content/bps-file.csv',delimiter =';')
data
angka = data['data_content']
angka
def rumus_a(sumy, sumx, sumx2, sumxy):
  a = ((sumy * sumx2)-(sumx * sumxy)) / ((12 * sumx2)-(sumx*sumx))
  return a
def rumus_b(sumy, sumx, sumx2, sumxy):
  b = ((12 * sumxy)-(sumx * sumy)) / ((12 * sumx2)-(sumx*sumx))
  return b
sumx = sumx2 = 0
for i in range(1,13):
  sumx = sumx + i
  x2 = i*i
  sumx2 = sumx2 + x2
sumpy = sumty = sumjy = sumsy = 0
sumpxy = sumtxy = sumjxy = sumsxy = 0
j = 1 #bulan awal
for i in range(0, len(angka), 4):
  sumpy = sumpy + angka[i]
  sumpxy = sumpxy + (angka[i] * j)
  sumty = sumty + angka[i+1]
  sumtxy = sumtxy + (angka[i+1] * j)
  sumjy = sumjy + angka[i+2]
  sumjxy = sumjxy + (angka[i+2] * j)
  sumsy = sumsy + angka[i+3]
  sumsxy = sumsxy + (angka[i+3] * j)
  j += 1
pa = rumus_a(sumpy, sumx, sumx2, sumpxy)
ta = rumus_a(sumty, sumx, sumx2, sumtxy)
ja = rumus_a(sumjy, sumx, sumx2, sumjxy)
sa = rumus_a(sumsy, sumx, sumx2, sumsxy)
pb = rumus_b(sumpy, sumx, sumx2, sumpxy)
tb = rumus_b(sumty, sumx, sumx2, sumtxy)
jb = rumus_b(sumjy, sumx, sumx2, sumjxy)
sb = rumus_b(sumsy, sumx, sumx2, sumsxy)
print ('regresi linear produksi   => Y = %.0f + %.0f*X' %(pa, pb))
print ('regresi linear terpasang  => Y = %.0f + %.0f*X' %(ta, tb))
print ('regresi linear terjual    => Y = %.0f + %.0f*X' %(ja, jb))
print ('regresi linear susut      => Y = %.0f + %.0f*X' %(sa, sb))
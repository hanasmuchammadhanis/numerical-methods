#ndd1
import math
def product_term(i, nilai, a):  
    product = 1   
    for j in range(i):  
        product = product * (nilai - a[j])   
    return product   
def  tabel(a, b, n): 
    for i in range(1, n):  
        for j in range(n - i):  
            b[j][i] = ((b[j][i - 1] - b[j + 1][i - 1]) /(a[j] - a[i + j]))  
    return b  
def  rumus(nilai, a, b, n):  
    jumlah = b[0][0]
    for i in range(1, n): 
        jumlah = jumlah + (product_term(i, nilai, a) * b[0][i])   
    return jumlah    
def menampilkan_tabel(b, n):  
    for i in range(n):  
        for j in range(n - i):  
            print(round(b[i][j], 4), "\t",   end = " ")   
        print("")   
orde    = int (input("orde = "))
n       =   orde + 1
b       = [[0 for i in range(n)] for j in range(n)]  
a       = [ 1, 4, 6, 7]   
b[0][0] =  math.log10(a[0])
b[1][0] =  math.log10(a[1])
b[2][0] =  math.log10(a[2])
b[3][0] =  math.log10(a[3])
b       = tabel(a, b, n)  
nilai   = int(input("a    = "))
print("nilai analitik log a =", math.log10(nilai))
et = abs((rumus(nilai, a, b, n)-math.log10(nilai))/math.log10(nilai)*100)
menampilkan_tabel(b, n)
print("nilai numerik log a  =",rumus(nilai, a, b, n))
print("nilai toleransi (%) = ", et)

#ndd2
import numpy
def product_term(i, nilai, a):  
    product = 1   
    for j in range(i):  
        product = product * (nilai - a[j])   
    return product   
def  tabel(a, b, n): 
    for i in range(1, n):  
        for j in range(n - i):  
            b[j][i] = ((b[j][i - 1] - b[j + 1][i - 1]) /(a[j] - a[i + j]))  
    return b  
def  rumus(nilai, a, b, n):  
    jumlah = b[0][0]
    for i in range(1, n): 
        jumlah = jumlah + (product_term(i, nilai, a) * b[0][i])   
    return jumlah     
def menampilkan_tabel(b, n):  
    for i in range(n):  
        for j in range(n - i):  
            print(round(b[i][j], 4), "\t",   end = " ")   
        print("")   
n = int(input('Masukan berapa titik x yang digunakan = '))
x = numpy.zeros([n])
y = numpy.zeros([n, n])
i = 0 
while (i < n):
    x[i]= int(input("x%i = " %(i)))
    y[i][0] = float(input("y%i = " %(i)))
    i = i + 1
banyak_data = int(input("jumlah data x yang akan dihitung = "))
nilai = numpy.zeros([banyak_data])
perulangan = 0
while (perulangan < banyak_data):
    nilai[perulangan] = int(input('masukan nilai x yang akan dihitung = '))
    perulangan = perulangan + 1
menampilkan_tabel(b, n)
perhitungan = 0
while (perhitungan < banyak_data):
    y = tabel(a, b, n)
    perhitungan = perhitungan + 1
akhir = 0 
while (akhir < banyak_data):
    print("nilai dari numerik", nilai[akhir]," = ", round(rumus(nilai[akhir],a, b,n), 3))
    akhir = akhir + 1
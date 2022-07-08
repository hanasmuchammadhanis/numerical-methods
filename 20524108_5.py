#Newton-Raphson 
z        = int (input ("Tiga digit NIM terakhir: "))
x1       = float (input ("x = "))
maksimal = int (input("maksimal iterasi: "))
iterasi  = 0
while iterasi <= maksimal:
  fx1     = x1*x1 - z
  dif_fx1 = 2*x1
  x2      = x1 - (fx1/dif_fx1)
  print("iterasi ke-%i = %f \t fx = %.3f \t f'x = %.3f \t x(i+1) = %.3f" %(iterasi, x1, fx1, dif_fx1, x2))
  x1 = x2
  if abs (dif_fx1) <= 0.001:
    iterasi = maksimal
  iterasi += 1

  #Secant
z        = int (input ("Tiga digit NIM terakhir: "))
x1       = float (input ("x1 = "))
x2       = float (input ("x2 = "))
maksimal = int (input("maksimal iterasi: "))
iterasi  = 0
while iterasi <= maksimal:
  fx1 = x1*x1 - z
  fx2 = x2*x2 - z
  x3  = x2 - ((fx2*(x2-x1))/(fx2-fx1))
  print("iterasi ke-%i = %f \t fx = %.3f \t f'x = %.3f \t x(i+1) = %.3f" %(iterasi, x1, fx1, dif_fx1, x2))
  x1 = x2
  x2 = x3
  if abs (fx1) <= 0.001:
    iterasi = maksimal
  iterasi += 1
function y = fungsi(x)
  y = x^3 - 0.165*x^2 - (3.993*10^-4);
 end
clear all; clc; close all;
xl = 0;
xu = 0.11;
ErrorToleransi = 0.0001;
ErrorRelatif = 1;
xmn = 1;
iterasi = 0;
fprintf("=============================================================\n")
fprintf("Iterasi    xm \t\tErrorRelatif    \tInterval \n")
fprintf("=============================================================\n")
while ErrorRelatif > ErrorToleransi
  iterasi = iterasi + 1;
  xm = (xl + xu)/2;
  Fbawah = fungsi(xl);
  Ftengah = fungsi(xm);
  if Fbawah * Ftengah == 0
    disp('xm adalah akar');
  elseif Fbawah * Ftengah < 0
    xu = xm;
  else 
    xl = xm;
  end
  ErrorRelatif = abs((xmn - xm)/xmn);
  fprintf('%d \t%f \t%f \t(%f ; %f) \n', iterasi, xm, ErrorRelatif, xl, xu); 
  xmn = xm;
end
fprintf('\nAkarnya adalah %f pada iterasi ke %d \n', xm, iterasi)
clear all; clc; close all;
xl = 0;
xu = 0.11;
ErrorToleransi = 0.0001;
ErrorRelatif = 1;
xmn = 1;
iterasi = 0;
fprintf("=============================================================\n")
fprintf("Iterasi    xm \t\tErrorRelatif    \tInterval \n")
fprintf("=============================================================\n")
while ErrorRelatif > ErrorToleransi
  iterasi = iterasi + 1;
  Fbawah = fungsi(xl);
  Fatas  = fungsi(xu);
  xm = xu - (( Fatas*(xu - xl))/(Fatas-Fbawah));
  Ftengah =fungsi(xm);
  if Fbawah * Ftengah == 0
    disp('xm adalah akar');
  elseif Fbawah * Ftengah < 0
    xu = xm;
  else 
    xl = xm;
  end
  ErrorRelatif = abs((xmn - xm)/xmn);
  fprintf('%d \t%f \t%f \t(%f ; %f) \n', iterasi, xm, ErrorRelatif, xl, xu); 
  xmn = xm;
end
fprintf('\nAkarnya adalah %f pada iterasi ke %d \n', xm, iterasi)
#! /usr/bin/python
#!encoding: UTF-8
pi = 3.1415926535897931159979634685441852
def piaprox(n):
  suma = 0
  if (n!=0):
    for i in range(1,n+1):
      #a = float (i-1)/n
      #b = float(i)/n
      #print 'Subintervalo: (%f , %f) ' % (a, b)
      x = (i-0.5)/n
      f = 4/(1+x*x)
      suma = suma + f
  aprox = suma / n
  return aprox

veces = int (raw_input('Introduce el número de veces que quiere ejecutar el programa '))
n = int (raw_input('Introduce el valor de subintervalos '))
a = []
for vez in range (1,veces+1):
  unaAprox = piaprox(n*vez)
  a=a+[unaAprox]
  print "%.15g" % unaAprox
print a

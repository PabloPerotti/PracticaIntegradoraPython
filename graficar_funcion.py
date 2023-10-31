import matplotlib.pyplot as plt
import math

def f(x):
  return math.sin( 2 * math.pi * x )

n = 50  

X = [ x/(n-1) for x in range(n) ] 
Y = [ f(x) for x in X ]

plt.plot(X, Y)   
plt.show()
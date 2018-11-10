import math
import cmath
z0 = input("\nWhat is the c value?\n")
z0 = z0.replace("i", "j")
z0 = complex(z0)
z = z0
c = z0
for n in range(10):
    z = z*z +  c
    print ('N{} = '.format(n+1) + '{0.real:.3f} + {0.imag:.3f}i'.format(z))

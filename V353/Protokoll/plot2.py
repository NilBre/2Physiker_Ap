import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([10.00,15.00,30.00,50.00,80.00,100.0,140.0,180.0,210.0,270.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000,1500,2000,3000,5000,10000,20000])
y = np.array([968,975,977,954,912,878,804,729,675,583,543,438,364,309,268,237,211,190,127,95,62,39.53,19.81,9.90])

#Umrechnung in Volt
y= y/1000;

xl = np.log(x)
y2 = y;
def f(q, a):
    #wegen omega=2*pi*f und hier ist q=f
    return 1 / np.sqrt(1 + (2*np.pi*q*a)**2 )

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
plt.xscale ('log')
plt.plot(x,y, 'k.', label="Gemessene Werte")
plt.plot(x, f(x, *params), 'r-', label="Ausgleichsfunktion")
plt.xlabel(r'$\nu /$ Hz ')
plt.ylabel(r'$A/ $ V')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')

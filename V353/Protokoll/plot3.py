import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([10.00, 15.00, 20.00, 25.00, 30.00, 50.00, 100.0, 250.0, 500.0, 1000.0, 5000.0])
y = np.array([0, 0, 0.10, 0.13, 0.15, 0.25, 0.44, 0.85, 1.23, 1.26, 1.64])

def f(q, a):
    #return np.arctan(-q*a)
    #wegen omega=2*pi*f und hier ist q=f
    return np.arctan(-2*np.pi*q*a)

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
plt.xscale ('log')
plt.plot(x,y, 'k.', label="Gemessene Werte")
plt.plot(x, f(x, *params), 'r-', label="Ausgleichsfunktion")
plt.xlabel(r'$\nu /$ Hz ')
plt.ylabel(r'$\phi /$ rad ')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([170.0, 160.0, 140.0, 130.0, 120.0, 76.0, 71.0, 65.0, 61.5, 57.5, 54.5, 51.0, 48.5, 47.0, 45.0, 43.0, 41.0, 39.0, 38.0, 37.0, 36.0])
y = np.array([3.5, 3.4, 3.1, 2.9, 2.8, 2.6, 2.55, 2.43, 2.37, 2.31, 2.25, 2.22, 2.16, 2.13, 2.10, 2.07, 2.04, 2.01, 1.98, 1.98, 1.95])
x_plot = np.linspace(36,170)

def f(x, a, b):
    return a * x + b

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, 'bx', label='Messwerte', markersize=4)
plt.plot(x_plot, f(x_plot, *params), 'r-', label='linearer Fit', linewidth=0.5)
plt.legend(loc='best')
plt.xlabel(r'$I / \si{\milli\ampere}$')
plt.ylabel(r'$U_k / \si{\volt} $')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')

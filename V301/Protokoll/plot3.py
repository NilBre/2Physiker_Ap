import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([7.5, 7.4, 6.3, 5.6, 5.2, 4.7, 4.3, 4.0, 3.8, 3.5, 3.3, 3.1, 3.0, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1])
y = np.array([110, 115, 230, 260, 290, 320, 350, 355, 370, 380, 390, 400, 410, 420, 425, 430, 440, 440, 445, 450, 450])
x_plot = np.linspace(2.1, 7.5)

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
plt.savefig('build/plot3.pdf')

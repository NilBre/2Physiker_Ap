import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([1.11, 1.08, 0.99, 0.78, 0.63, 0.57, 0.51, 0.45, 0.40, 0.36, 0.35, 0.31, 0.29, 0.27, 0.25, 0.23, 0.21, 0.20, 0.18, 0.17, 0.16])
y = np.array([300, 320, 380, 530, 630, 690, 740, 780, 810, 830, 850, 870, 880, 900, 910, 920, 940, 950, 955, 960, 970])
x_plot = np.linspace(0.15, 1.11)

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
plt.savefig('build/plot4.pdf')

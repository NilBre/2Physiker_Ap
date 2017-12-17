import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([86, 83, 67, 61.5, 54, 48, 43, 37, 34, 33, 30, 28, 27, 26, 25, 23, 22, 21, 20, 19, 19])
y = np.array([0.05, 0.13, 0.38, 0.47, 0.59, 0.69, 0.71, 0.77, 0.80, 0.87, 0.90, 0.92, 1.00, 0.96, 0.99, 0.99, 1.02, 1.05, 1.05, 1.08, 1.08])
x_plot = np.linspace(86,19)

def f(x, a, b):
    return a * x + b

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, 'bx', label='Messwerte', markersize=4)
plt.plot(x_plot, f(x_plot, *params), 'r-', label='linearer Fit', linewidth=0.5)
plt.legend(loc='best')
plt.xlabel(r'Stromstärke $I / \si{\milli\ampere}$')
plt.ylabel(r'Klemmenspannung $U_k / \si{\volt} $')
plt.grid()

#x = np.linspace(0, 10, 1000)
#y = x ** np.sin(x)
#
#plt.subplot(1, 2, 1)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
#plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
#plt.legend(loc='best')
#
#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
#plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
#plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

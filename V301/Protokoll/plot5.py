import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.linspace(0.0, 50.0, 21)
y = np.array([0, 0.0172225, 0.022445, 0.02837, 0.02916, 0.0288, 0.027735, 0.0239575, 0.023805, 0.0245025, 0.0225, 0.02156, 0.02187, 0.02197, 0.021875, 0.02071, 0.01936, 0.0187425, 0.018, 0.0171475, 0.01805])

y= y*1000

def f(x):
    return ((1.35*1.35)*x)/((x+14.67)*(x+14.67))*1000

#errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, 'bx', label='Messwerte', markersize=4)
#plt.plot(x_plot, f(x_plot, *params), 'r-', label='linearer Fit', linewidth=0.5)
plt.plot(x, f(x), 'r-', label='Theoriekurve', linewidth=0.5)
plt.legend(loc='best')
plt.xlabel(r'$R_a / \si{\Omega}$')
plt.ylabel(r'$P / \si{mW}$')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot5.pdf')

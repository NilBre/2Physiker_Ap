import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.linspace(0.06, 0.38, 17)
y = np.array([5.36,5.12,4.72,4.40,4.16,3.92,3.60,3.32,3.08,2.84,2.64,2.32,2.12,1.96,1.72,1.44,1.20])

#x = np.array([0.10,0.20,0.35,0.50,1.0,1.2,1.4,1.6,1.8])
#y = np.array([4.00,3.75,3.50,3.00,2.00,1.75,1.50,1.25,1.10])

y= np.log(y)

def f(x, a, b):
    return -1/a * x + b

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))

#Linear Regression1
#fit = np.polyfit(x,y,1)
#fit_fn = np.poly1d(fit)
# fit_fn is now a function which takes in x and returns an estimate for y
#slope, intercept = fit
#print(slope)
plt.plot(x,y, 'kx', label="Gemessene Werte")
#plt.plot(x, fit_fn(x), '--k', label="Linearer Fit")
plt.plot(x, f(x, *params), 'r-', label="Linearer Fit")

#plt.subplot(1, 2, 1)
#plt.plot(x,y,'gx', label='Kurve')
#plt.axis('scaled')
plt.xlabel(r'$t \:/\: \si{10^{-3} \second}$')
plt.ylabel(r'$ln(U_c/U_0) \:/\: \si{\volt}$')
plt.legend(loc='best')
plt.grid(True)


#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
#plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
#plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

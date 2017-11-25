import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#x = np.array([0, 0, 0.10, 0.13, 0.15, 0.25, 0.44, 0.85, 1.23, 1.26, 1.64])
#w = np.array([10.00, 15.00, 20.00, 25.00, 30.00, 50.00, 100.0, 250.0, 500.0, 1000.0, 5000.0])
#y = -np.sin(x)/(w*0.004)
#x = x*2*np.pi
#theta = np.linspace(0, 1.7, 50)
nu = np.linspace(0,5000,50000)
w = nu*2*np.pi
ws = w**2
rc = 0.0007474
Awmuster = 1 / (np.sqrt(1+(ws*rc)**2))
sinphi = ws*rc/(np.sqrt(1+(ws*rc)**2))
#theta = 2 * np.pi * r
phi = np.array([0, 0, 0.1, 0.13, 0.15, 0.25, 0.44, 0.85, 1.23, 1.26, 1.64])
AwU0 = np.array([0.998899175, 0.997528242, 0.995618385, 0.993178897, 0.990221511, 0.973523738, 0.905161199, 0.648434404, 0.391833775, 0.208274986, 0.042550388])


plt.polar(AwU0, np.sin(phi), 'kx', label = 'Messwerte')
plt.polar(Awmuster, sinphi, 'r', label = 'Theoriekurve')


#plt.polar(x, y, xunits='radians')
plt.savefig('build/plot4.pdf')

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.linspace(0.80, 5.00, 22)
y = np.array([5.12,4.72,4.40,4.16,3.92,3.60,3.32,3.08,2.84,2.64,2.32,2.12,1.96,1.72,1.44,1.20,1.0,0.84,0.72,0.52,0.24,0.04])
y= np.log(y/5.12)

def f(x, a, b):
    return -1/a * x + b

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
print('a1 =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('a1 =', -1/params[0], '±', errors[0])

x2 = np.array([10.00,15.00,30.00,50.00,80.00,100.0,140.0,180.0,210.0,270.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000,1500,2000,3000,5000,10000,20000])
y2 = np.array([968,975,977,954,912,878,804,729,675,583,543,438,364,309,268,237,211,190,127,95,62,39.53,19.81,9.90])
#x2 = x2/1000

def g(q, a):
    return 968 / np.sqrt(1 + (q*a)**2 )

params, covariance_matrix = curve_fit(g, x2, y2)
errors = np.sqrt(np.diag(covariance_matrix))

print('a2 =', params[0], '±', errors[0])

x3 = np.array([10.00, 15.00, 20.00, 25.00, 30.00, 50.00, 100.0, 250.0, 500.0, 1000.0, 5000.0])
y3 = np.array([0, 0, 0.10, 0.13, 0.15, 0.25, 0.44, 0.85, 1.23, 1.26, 1.64])

def h(q, a):
    return np.arctan(-q*a)

params, covariance_matrix = curve_fit(h, x3, y3)
errors = np.sqrt(np.diag(covariance_matrix))



print('a3 =', params[0], '±', errors[0])

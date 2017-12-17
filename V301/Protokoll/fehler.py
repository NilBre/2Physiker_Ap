import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([86, 83, 67, 61.5, 54, 48, 43, 37, 34, 33, 30, 28, 27, 26, 25, 23, 22, 21, 20, 19, 19])
y = np.array([0.05, 0.13, 0.38, 0.47, 0.59, 0.69, 0.71, 0.77, 0.80, 0.87, 0.90, 0.92, 1.00, 0.96, 0.99, 0.99, 1.02, 1.05, 1.05, 1.08, 1.08])

def f(x, a, b):
    return b - x * a

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

print('a =', params[0]*1000, '±', errors[0]*1000)
print('b =', params[1], '±', errors[1])

x2 = np.array([170.0, 160.0, 140.0, 130.0, 120.0, 76.0, 71.0, 65.0, 61.5, 57.5, 54.5, 51.0, 48.5, 47.0, 45.0, 43.0, 41.0, 39.0, 38.0, 37.0, 36.0])
y2 = np.array([3.5, 3.4, 3.1, 2.9, 2.8, 2.6, 2.55, 2.43, 2.37, 2.31, 2.25, 2.22, 2.16, 2.13, 2.10, 2.07, 2.04, 2.01, 1.98, 1.98, 1.95])

def f(x, a, b):
    return b + x * a

params, covariance_matrix = curve_fit(f, x2, y2)

errors = np.sqrt(np.diag(covariance_matrix))

print('a2 =', params[0]*1000, '±', errors[0]*1000)
print('b2 =', params[1], '±', errors[1])

x3 = np.array([7.5, 7.4, 6.3, 5.6, 5.2, 4.7, 4.3, 4.0, 3.8, 3.5, 3.3, 3.1, 3.0, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1])
y3 = np.array([110, 115, 230, 260, 290, 320, 350, 355, 370, 380, 390, 400, 410, 420, 425, 430, 440, 440, 445, 450, 450])

def f(x, a, b):
    return b - x * a

params, covariance_matrix = curve_fit(f, x3, y3)

errors = np.sqrt(np.diag(covariance_matrix))

print('a3 =', params[0], '±', errors[0])
print('b3 =', params[1], '±', errors[1])

x4 = np.array([1.11, 1.08, 0.99, 0.78, 0.63, 0.57, 0.51, 0.45, 0.40, 0.36, 0.35, 0.31, 0.29, 0.27, 0.25, 0.23, 0.21, 0.20, 0.18, 0.17, 0.16])
y4 = np.array([300, 320, 380, 530, 630, 690, 740, 780, 810, 830, 850, 870, 880, 900, 910, 920, 940, 950, 955, 960, 970])

def f(x, a, b):
    return b - x * a

params, covariance_matrix = curve_fit(f, x4, y4)

errors = np.sqrt(np.diag(covariance_matrix))

print('a4 =', params[0], '±', errors[0])
print('b4 =', params[1], '±', errors[1])

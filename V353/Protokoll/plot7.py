import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.5*np.pi,3.5*np.pi,500)
x1 = np.linspace(0,np.pi,50)

plt.grid(linestyle='--')
plt.plot(x1, x1-0.5*np.pi,'r', label='Dreiecksfunktion')
plt.plot(x1+np.pi,-x1+0.5*np.pi,'r')
plt.plot(x1-np.pi,-x1+0.5*np.pi,'r')
plt.plot(x1-2*np.pi,x1-0.5*np.pi,'r')
plt.plot((0,np.pi), (0.4*np.pi,0.4*np.pi),'b', label='Vierecksfunktion')
plt.plot((np.pi,2*np.pi), (-0.4*np.pi,-0.4*np.pi),'b')
plt.plot((-np.pi,-2*np.pi), (0.4*np.pi,0.4*np.pi),'b')
plt.plot((0, -np.pi), (-0.4*np.pi,-0.4*np.pi),'b')
plt.plot((0, 0), (-0.4*np.pi,0.4*np.pi),'b--')
plt.plot((np.pi, np.pi), (-0.4*np.pi,0.4*np.pi),'b--')
plt.plot((-np.pi, -np.pi), (-0.4*np.pi,0.4*np.pi),'b--')

plt.legend()
plt.ylim((-0.6*np.pi,0.6*np.pi))
plt.xlim((-2*np.pi,2*np.pi))
plt.tick_params(
    axis='both',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off',
    right='off',
    left='off',
    labelleft='off')
plt.savefig('build/plot7.pdf')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.5*np.pi,3.5*np.pi,500)

plt.grid(linestyle='--')
plt.plot(x,np.sin(x),'b', label=r'$f(x)=sin(x)$')
plt.plot(x,np.cos(x),'r', label=r'$F(x)=cos(x)$')
plt.legend()
plt.ylim((-1.5,1.5))
plt.xlim((-3.5*np.pi,3.5*np.pi))
plt.tick_params(
    axis='both',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off',
    right='off',
    left='off',
    labelleft='off')
plt.savefig('build/plot5.pdf')

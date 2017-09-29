import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,100)
plt.plot(x, np.sin(x),"r-", label=r"$\sin(x)$")
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()

import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt

x=np.linspace(0,10,50)
y=np.sin(x)
z=y+np.random.normal(size=50)*.2
plt.plot(x,y,'o-',label="Regular Sine Wave")
plt.plot(x,z,'-',label="Noisy Sine Wave")
plt.legend(loc='lower right')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

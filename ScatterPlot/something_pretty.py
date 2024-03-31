#use random number generator to plot scatters of different colors
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
colours = np.random.randint(100,size=(100))
sizes = 10*np.random.randint(100,size=(100))

plt.scatter(x,y, c=colours, s=sizes, cmap='nipy_spectral', alpha = 0.7)
plt.title("Something Pretty :)")
plt.colorbar()
plt.show()
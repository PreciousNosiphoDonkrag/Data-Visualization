import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,2,17,2,9,7,11,12,9,6])
y = np.array([12,11,14,15,16,17,18,13,18,12,11,21])

#scatter requires both arrays to have the same length
plt.scatter(x,y, c = 'orange')

x = np.array([6,6,7,3,18,3,10,9,12,11,8,7])
y = np.array([11,10,15,14,18,14,19,15,20,10,13,23])
colors = np.arange(len(x)) 
#scatter requires both arrays to have the same length
plt.scatter(x,y,c=colors, cmap='viridis')
plt.title("Exploring plt.Scatter")
plt.show()

#2nd plot
x = np.array([5,7,8,2,17,2,9,7,11,12,9,6])
y = np.array([12,11,14,15,16,17,18,13,18,12,11,21])
colors = np.arange(len(x)) 

sizes = np.array([12,110,40,15,1600,17,80,13,181,45,11,21])
#scatter requires both arrays to have the same length
plt.scatter(x,y,c=colors, s = sizes,cmap='viridis', alpha=0.8)
plt.title("Exploring plt.Scatter")
plt.show()
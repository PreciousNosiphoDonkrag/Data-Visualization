import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_wine

wine = load_wine()
data = wine.data

print(wine.feature_names)
#these are the features for each wine bottle
#['alcohol', 'malic_acid', 'ash', 
# 'alcalinity_of_ash', 'magnesium',
#  'total_phenols', 'flavanoids', 
# 'nonflavanoid_phenols', 'proanthocyanins',
#  'color_intensity', 'hue', 
# 'od280/od315_of_diluted_wines', 'proline']

#i would like to view the most frequent alcohol %
#For personal reasons.
#this is column holds continuous data
#thus making it suitable to be modeled 
#using a histogram.
#alcohol is at index "0"
plt.hist(data[:,0], color="#7B0323", edgecolor="black")
plt.xlabel("Alcohol Content")
plt.ylabel("Frequency")
plt.title("Wine Histogram")
plt.show()

#From the histogram we can see that
#the most frequent alcohol % is around 12.5
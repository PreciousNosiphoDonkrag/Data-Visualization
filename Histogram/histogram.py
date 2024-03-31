import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_wine
from scipy.stats import skew
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


#The histogram is a statistical model. so lets add stats on out plot
mean = np.mean(data[:,0])
median = np.median(data[:,0])
std = np.std(data[:,0])
#to get the mode we find the max frequency
#then count the number of variables that make up this max freq.
#mode = np.argmax(np.bincount(data[:,0].astype(int)))
#mode not required for continous data

#skewness
skewness = skew(data[:,0])

#just plot vertical lines to show the mean and median
plt.axvline(mean, color="blue", linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
plt.axvline(median, color="green", linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
x_coordinate = 11
y_coordinate = 35
plt.text(x_coordinate, y_coordinate, f'Skewness: {skewness:.2f}', fontsize=10, verticalalignment='top')
plt.legend()
plt.show()
#This section will use a readily available
#dataset from sklearn to plot the scatter plot
#the relationship we are trying to view
#is between the BMI (body mass index) and the progression of diabetes
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import pandas as pd

#All supervised datasets in sklearn come with a target dataset
#this must be isolated as it is one of the variables who's relationship
#is to be visualised
diabetes_data = load_diabetes()
diabetes_prog = diabetes_data.target #y-axis
data = diabetes_data.data

#lets view all the feautres of the dataset before beggining
#in the attempt to further understand the dataset
print(diabetes_data.feature_names) #the output is ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

#for the curious Gee the S1..S6 are specific blood works related to some specific chemicals.

#upon further exploration of the dataset i am now interested
#in viewing the relationship between Blood pressure(bp) and diabetes progression so we pivot.

#The pb is in clomun "3"
plt.title("The relationship between Blood pressure and Diabetes progression")
plt.scatter(data[:,3], diabetes_prog, c=diabetes_prog,cmap="rainbow", alpha=0.5)
plt.xlabel("Blood Pressure")
plt.ylabel("Diabetes prgression")
plt.show()
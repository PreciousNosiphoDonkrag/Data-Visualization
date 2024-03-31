#This section will use a readily available
#dataset from sklearn to plot the scatter plot
#the relationship we are trying to view
#is between the BMI (body mass index) and the progression of diabetes
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import pandas as pd
from scipy.stats import linregress

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

# Calculate the coefficients of the linear regression model
slope, intercept, r_value, p_value, std_err = linregress(data[:, 3], diabetes_prog)
# the linregress accepts 2 input parameters the x and y
# it returns 5 output parameters :
# 1. the gradient
# 2. y-intercept
# 3. r-correlation coefficient (measures stregnth and direction of the linear function)
# 4. p_value: The two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero, indicating no relationship between the variables. A low p-value (< 0.05) suggests that the relationship is statistically significant.
# 5. std_err: standard error of estimating the gradient

# Plot the line of best fit
plt.plot(data[:, 3], slope * data[:, 3] + intercept, color='black', linestyle='-', linewidth=1)

plt.show()
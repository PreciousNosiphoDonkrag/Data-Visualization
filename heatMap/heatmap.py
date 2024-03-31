import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Get the current directory of the Python script
current_dir = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(current_dir, "titanic.csv")
titanic_df = pd.read_csv(file_path) 

#Exploring the dataset
#print(titanic_df.columns)
#Index(['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
#       'Parents/Children Aboard', 'Fare'],
#      dtype='object')
#print(titanic_df.head(10))

#drop rows with missing values
titanic_df.dropna(inplace=True)

#Heatmaps are a form of correlation analysis so thry require numeric data
#select the numeric features to correlate
features = ['Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']

# computes the correlation coefficients between all pairs of numerical features in the DataFrame.
corr_matrix = titanic_df[features].corr()

plt.figure(figsize=(15,15))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
#annot to just show the correlation coefficient for the variables
plt.title('Correlation Heatmap of Titanic Dataset Numerical Features')
plt.yticks(rotation=0)  # Rotate y-axis tick labels to be horizontal
plt.show()
# Heatmap
## What is a Heatmap?
A heatmap is a graphical representation of data where the values of a matrix are represented as colors. It provides a visual summary of the data by displaying colours that correspond to different values. Heatmaps are particularly useful for identifying patterns, trends, and correlations in datasets.

## When to Use a Heatmap 
Exploring Relationships <br>
Heatmaps are ideal for exploring relationships between variables in a dataset. They allow you to visually assess the strength and direction of correlations between variables.

Detecting Patterns <br>
Heatmaps help in detecting patterns and trends in data, such as clusters or gradients. They provide a visual summary of complex datasets, making it easier to identify important features.

Comparing Multiple Variables <br>
Heatmaps can be used to compare multiple variables simultaneously by visualizing their relationships in a single plot. This makes it easier to identify correlations and dependencies between variables.

Visualizing Multivariate Data <br>
Heatmaps can visualize multivariate data by encoding additional variables using color intensity or saturation. This allows for the exploration of relationships between multiple variables at once.

## When Not to Use a Heatmap

Non-Numerical Data <br> 
Heatmaps are designed for visualizing numerical data. When dealing with non-numerical data, such as categorical or text data, other visualization techniques should be used.

Large Datasets <br>
For very large datasets, heatmaps may become overcrowded and difficult to interpret. In such cases, it may be necessary to use sampling techniques or other visualization methods to summarize the data effectively.

Categorical Variables <br>
Heatmaps are not suitable for visualizing relationships between categorical variables. In such cases, other types of plots, such as bar charts or stacked plots, may be more appropriate

## The current Heatmap
### The titanic.csv dataset from Kaggle was used for this project.
### About the dataset
The information about the features of the dataset is given below:
- Survived: Whether the passenger survived or not (0 = No, 1 = Yes).
- Pclass: The ticket class of the passenger (1 = 1st, 2 = 2nd, 3 = 3rd).
- Name: The name of the passenger.
- Sex: The gender of the passenger (male or female).
- Age: The age of the passenger.
- Siblings/Spouses Aboard: The number of siblings or spouses aboard the Titanic.
- Parents/Children Aboard: The number of parents or children aboard the Titanic.
- Fare: The fare paid by the passenger.

Heat maps require numeric data to find the correlation coefficients between variables. The following numeric features were chosen for the heatmap:
- Age: The age of the passenger.
- Siblings/Spouses Aboard: The number of siblings or spouses aboard the Titanic.
- Parents/Children Aboard: The number of parents or children aboard the Titanic.
- Fare: The fare paid by the passenger.
  
### The Heatmap
![Screenshot 2024-03-31 151513](https://github.com/PreciousNosiphoDonkrag/Data-Visualization/assets/153648767/262b3a15-5657-41a0-ba07-f1875c79d07d)
- Correlation coefficients
    * 1: this indicates a perfect positive correlation (as one variable increases          the other one also increases).
    * 0: indicates no correlation, meaning that there is no linear relationship              between the variables.
    * -1: indicates a perfect negative correlation, meaning that as one variable               increases, the other decreases. <br> <br>
    For the current heatmap, we see a slightly positive correlation between the         variables 'Fare' and 'Parents/Children Aboard' and this logically makes sense       because the more people on board for a specific family, the higher the fare. <br> <br>
    This was my first time working with a heatmap outside my project management course (the heatmap was the risk matrix), I found it to be an incredibly useful tool for analysis and I will be using more of it in the future.

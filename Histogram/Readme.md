# Histogram
What is a Histogram?
A histogram is a graphical representation of the distribution of numerical data. 
It consists of a series of contiguous rectangles, or bins, each representing 
**a range** of values and the height of each bin corresponds to the frequency
or count of data points within that range.

## When to Use a Histogram
1. Understanding Data Distribution <br>
   Histograms are ideal for visualizing the distribution of a dataset.
    They provide insights into the central tendency, dispersion,
   and shape of the data, allowing you to identify patterns, outliers,
   and underlying trends.

2. Identifying Skewness and Outliers <br>
   Histograms help in identifying skewness in the data distribution.
   Skewed distributions may be positively skewed (skewed to the right) or
   negatively skewed (skewed to the left), and histograms make it easy to visualize
   such patterns. Additionally, outliers, which are data points that deviate
   significantly from the rest of the data, can often be detected visually in a histogram.

3. Comparing Multiple Distributions <br>
   When you have multiple datasets or subgroups within a dataset,
   histograms allow for easy comparison of their distributions.
   By plotting multiple histograms on the same axis or using overlaid histograms,
   you can visually compare the distributions and discern any differences or similarities
   between them.
   
## When Not to Use a Histogram
 
 1. Discrete Data with Few Categories <br>
    For discrete data with only a few distinct categories,
    a histogram may not provide meaningful insights.
    In such cases, bar charts or other types of visualizations may be more suitable.

2. Unequal Bin Widths <br>
   Histograms rely on the choice of bin widths to display the data distribution
    accurately. If the bin widths are not chosen appropriately,
   the resulting histogram may distort the true nature of the data distribution.

4. Showing Relationships between Variables <br>
  Histograms are not suitable for showing relationships between multiple variables.

## The current Histogram
  The data used to plot this histogram came from the Sklean library, the dataset is called Load_wine.
  The frequency of different ranges of alcohol content in the dataset was plotted. some statistical measures were
  added to the plot: 
  ![wineHis](https://github.com/PreciousNosiphoDonkrag/Data-Visualization/assets/153648767/2f901417-57a1-41eb-9fb0-1a5a91ffb680)

  - The closeness of the values between the mean and median suggests that the dataset is likely
    symmetrically distributed.
  - the skewness of -0.05 tells us that there is a slight negative skewness in the dataset.
    from the dataset, this skewness tells us there is a slightly higher number of lower
    alcohol content wines than high alcohol content wines.
  - The histogram coupled with some statistical measures provided more insight into
    the dataset.

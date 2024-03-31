#In this section we practice the use of pandas library
#we read and filter out an excel file then 
#create a pie chart from the remaining unflitered data
#the excel file was downloaded from SARB website
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import os

# Get the current directory of the Python script
current_dir = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(current_dir, "Foodandbeveragesfrom2005.xlsx")
df = pd.read_excel(file_path)

#isolate the 2023 columns
col_2023 = []
for col in df.columns:
    if '2023' in col:
        col_2023.append(col)

#add the column with the food bev. names
col_2023.append('H04')
df_col_filtered = df[col_2023]
#now filter the rows and only look at coffee shops
        
#enumerate() allows you to interate over lists,arrays,tuples
#while simultaneously returning its index
#
result_list=[]

for index, name in enumerate(df_col_filtered['H04']):
    if 'Total income : Restaurants and coffee shops' in name:
        #print(f"index: {index}      name: {name}")
        start_idx = df_col_filtered.columns.get_loc('MO022023')
        end_idx = df_col_filtered.columns.get_loc('MO122023') + 1  # Adding 1 to include the end index
        result_list.append(df_col_filtered.iloc[index, start_idx: end_idx].values)
        
#Pie Plot
shops_Labels = ['Lalas coffee shop', 'Caffinate', 'Take a break.', 'Crystal Cup']
Total_Incomes = []
sum_total = 0
for array in result_list:
    for element in array:
        sum_total = sum_total + element
    Total_Incomes.append(round(sum_total, 2))
    sum_total = 0
print(Total_Incomes)  

colours = ['Pink', '#32cd32', 'green', 'purple']
plt.pie(Total_Incomes, colors=colours, labels= shops_Labels, autopct='%1.1f%%')
plt.title("Total income from coffee shops for the year 2023")
plt.show()
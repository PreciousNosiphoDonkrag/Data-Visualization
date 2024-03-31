#the Aim of this script is to plot a bar graph using the available json data
import json
import os
import numpy as np
import matplotlib.pyplot as plt
#accessing the file location using current dir
current_dir = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(current_dir, "data.json") 
#file_path = file_path.replace("\\", "/")

def plot_Bar(letters, freq, acc):
    #to avoid overlap, create an array of evenly spaced values corresponding
    #to the x-axis values
    num_of_varaibles = np.arange(len(letters))
    #now shift the respective bars 0.2 to each side
    plt.bar(num_of_varaibles-0.2, freq, 0.4, label="frequency", color="red")
    plt.bar(num_of_varaibles+0.2, acc, 0.4, label="Accuracy")
    
    plt.xticks(num_of_varaibles, letters) #specifies the position of the x-axis labels (position, label)
    plt.xlabel("Letters")
    plt.ylabel("Algorithm result")
    plt.title("Algorithm's output for handwritten letters")
    plt.legend() #show the legend for frequency and accuracy so you know which bar is which
    plt.show()


try: #check if the file opens
     with open(file_path, 'r') as file:
        data = json.load(file)

except:
    print("Problem encoutered when trying to open the data")  

#if the file has been successfully located and opened continue here
else:
    letters_list, frequencies_list,accuracy_list = [],[],[]
    for item in data:
        letters_list.append(item['Letter'])
        frequencies_list.append(item['Freq'])
        accuracy_list.append(item['Accuracy'])
    plot_Bar(letters_list, frequencies_list, accuracy_list)


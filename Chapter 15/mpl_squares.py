############################################
# Software Req Doc: Data Visualization
# Release Date: 10/23/24
# Sam Rodriguez
# Description: Requirement 2 Line Plot 
# Scatter Plot, Calculating Data Automatically
# Removing outliers, Saving
############################################

#Imports
import matplotlib.pyplot as plt

#Setting up the information
input_values = [1, 2, 3, 4, 5]
squares = [1 ,4, 9, 16, 25]

#Customization
plt.plot(input_values, squares, linewidth = 5)

#set Title and Label Axis
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
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

#calculating Data automatically
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#Try it yourself values Do everything with cubes
# x_values = list(range(1, 5000))
# y_values = [x**3 for x in x_values]

#plt.scatter(x_values, y_values, edgecolor='none', s=40)

#Custom Colors
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#plt.scatter(x_values, y_values, c=(0, 0, 0.8) ,edgecolor='none', s=40)

#Using A colormap (I like this one the best)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

#Set Title and Labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#Set the range 
# plt.axis([0, 1100, 0, 1100000])


#Set tick size of labels
plt.tick_params(axis='both', which='major', labelsize = 14)

#This wasn't in the book but it fixes things showing up in 
# scinotation so it'll look like the picture.
plt.ticklabel_format(style='plain')

plt.show()
#To save instead of show use SAVEFIG
# plt.savefig('squares_plot.png', bbox_inches='tight')
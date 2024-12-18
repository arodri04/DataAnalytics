############################################
# Software Req Doc: Data Visualization
# Release Date: 10/23/24
# Sam Rodriguez
# Description: Requirement 3, Creating a random 
# walk class that chooses a random direction 
# and stores the points.
############################################


import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks
while True:
    #make a random walk and plot the points
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Set size of the plotting window
    plt.figure(dpi=128, figsize=(10,6))
    
    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # plt.scatter(rw.x_values, rw.y_values, s=15)
    #Emphasize the first and last
    plt.scatter(0, 0, c="green", edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)


    
    #remove axes #plt.axes() did not work needed to swap to gca
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
############################################
# Software Req Doc: Data Visualization
# Release Date: 10/23/24
# Sam Rodriguez
# Description: Requirement 3, Creating a random 
# walk class that chooses a random direction 
# and stores the points.
############################################

#Imports
from random import choice

class RandomWalk():
    """Class to Generate random walk"""

    def __init__(self, num_points=5000):
        """Initializa attributes of a walk."""
        self.num_points = num_points

        #start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    
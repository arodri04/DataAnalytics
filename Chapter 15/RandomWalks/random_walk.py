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

    def fill_walk(self):
        '''Calculate the walking points'''

        #Keep taking steps until walk is desired length
        while len(self.x_values) < self.num_points:
            #decide which direction to go and how far in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
    
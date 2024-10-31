from die import Die
import pygal

# #create two d6
die_1 = Die()
die_2 = Die()
# numOfDice = 2

#to add third die uncomment
die_3 = Die()
numOfDice = 3


#make rolls
results = []
rolls = 5000

for roll_num in range(rolls):
    #two dice
    # result = die_1.roll() + die_2.roll()
    #Three dice result, uncomment
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)



#analyze results
frequencies = []
#Max Results for 2 die
# max_result = die_1.num_sides + die_2.num_sides

#Max results for 3 dice, uncomment
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides



for value in range(numOfDice, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#visualize results
hist = pygal.Bar()

hist.title = f"results of rolling 3d6 {rolls} times."

#use list comprehension to automatically make the x label
hist.x_labels = [(x+numOfDice) for x in range(max_result-(numOfDice-1))]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('3d6', frequencies)
hist.render_to_file('die_visual.svg')
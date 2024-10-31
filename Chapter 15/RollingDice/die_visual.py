from die import Die
import pygal

#create two d6
die_1 = Die()
die_2 = Die(10)

#make rolls
results = []
rolls = 50000

for roll_num in range(rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

#analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#visualize results
hist = pygal.Bar()

hist.title = f"results of rolling a D6 and a D10 {rolls} times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
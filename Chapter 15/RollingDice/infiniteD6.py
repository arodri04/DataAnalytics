from die import Die
import pygal

numOfDice = int(input("How many D6 do you want to roll: "))
#Creating array of all d6
dice = [Die() for x in range(numOfDice)]



#make rolls
results = []
rolls = int(input(f"How many times do you want to roll {numOfDice}d6: "))

def roll_dice(dice):
    total = 0
    for die in dice:
        total += die.roll()
    return(total)
for i in range(rolls):
    result = roll_dice(dice)
    results.append(result)

#analyze results
frequencies = []


#Max Results for infinite d6
max_result = numOfDice*6

for value in range(numOfDice, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#visualize results
hist = pygal.Bar()

hist.title = f"results of rolling {numOfDice}d6 {rolls} times."

#use list comprehension to automatically make the x label
hist.x_labels = [(x+numOfDice) for x in range(max_result-(numOfDice-1))]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(f'{numOfDice}d6', frequencies)
hist.render_to_file('die_visual.svg')
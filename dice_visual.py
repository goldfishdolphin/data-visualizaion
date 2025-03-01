import plotly.express as px
from die import Die


die1 = Die()
die2 = Die()
die_results = []
for roll_num in range(100):
    die_result = die1.roll()+die2.roll()
    die_results.append(die_result)

for roll_num in range(1000):
    die_result = die1.roll()+ die2.roll()
    die_results.append(die_result)
frequencies = []
max_result = die1.num_sides+die2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = die_results.count(value)
    frequencies.append(frequency)
print(frequencies)

title = "Result of Rolling two Six Sided Die for 1000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x= poss_results, y = frequencies, title=title, labels=labels)
fig.write_image("histogram_2dice.png")


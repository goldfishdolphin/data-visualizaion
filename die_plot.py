import plotly.express as px
from die import Die


die = Die()
die_results = []
for roll_num in range(100):
    die_result = die.roll()
    die_results.append(die_result)

for roll_num in range(1000):
    die_result = die.roll()
    die_results.append(die_result)
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = die_results.count(value)
    frequencies.append(frequency)
print(frequencies)

title = "Result of Rolling One Six Sided Die for 1000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x= poss_results, y = frequencies, title=title, labels=labels)
fig.write_image("histogram_die.png")


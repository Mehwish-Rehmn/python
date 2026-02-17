'''
matplotlib:
 the most popular python library for making charts, graphs, plots.
it's like drawing pictures with numbers.
'''
# you install it once:
# pip install matplotlib

import matplotlib.pyplot as plt   # everyone uses plt as short name


# example 1 – basic line plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y)
plt.show()
# this draws a simple line connecting the points.

# example 2 – add title, labels, and style
import matplotlib.pyplot as plt
months = ["jan", "feb", "mar", "apr", "may"]
sales = [120, 150, 180, 140, 200]
plt.plot(months, sales, color="blue", marker="o", linestyle="--")
plt.title("monthly sales 2026")
plt.xlabel("month")
plt.ylabel("sales in thousands")
plt.grid(True)
plt.show()
# now it looks like a proper chart.

#example 3 – bar chart (very common)
import matplotlib.pyplot as plt

cities = ["delhi", "mumbai", "bangalore", "chennai"]
population = [32000, 21000, 13000, 11000]

plt.bar(cities, population, color=["red", "blue", "green", "orange"])
plt.title("population of cities (in thousands)")
plt.xlabel("city")
plt.ylabel("population")
plt.show()

'''
5 most useful concepts 

plt.plot()- line graph
plt.bar()- bar chart
plt.scatter()- dots for points
plt.hist()- histogram for distribution
plt.title(), xlabel(), ylabel()- labels
plt.show()- actually show the chart
plt.savefig("chart.png")- save as image'''

# practice 
import matplotlib.pyplot as plt

days = ["mon", "tue", "wed", "thu", "fri"]
study_hours = [2, 4, 6, 3, 5]

plt.plot(days, study_hours, marker="o", color="purple")
plt.title("study hours this week")
plt.xlabel("day")
plt.ylabel("hours")
plt.grid(True)
plt.show()
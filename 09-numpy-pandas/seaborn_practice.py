"""what is seaborn?
seaborn is a python library that makes beautiful and easy statistical charts.
it's built on top of matplotlib (which we talked about earlier), but seaborn does the hard work for you:
-prettier defaults
-less code for complex plots
-smart colors and themes
-great for showing patterns in data
"""
#you install it once:
#pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt   # you still need this

"""
why people love seaborn

one line makes nice looking charts
automatic good colors
works perfectly with pandas dataframes
built-in themes (darkgrid, whitegrid, etc.)
statistical plots like heatmaps, pair plots, violin plots come ready
"""

# basic plot
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")   # built-in dataset (free)
sns.lineplot(data=tips, x="total_bill", y="tip")
plt.title("tip vs total bill")
plt.show()

# scatter block wiyh category
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")
plt.title("tips by bill amount and day")
plt.show()  #hue = color by category.   style = different markers

# box plot
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("bill amount by day and gender")
plt.show()


#heatmap
import numpy as np
# fake correlation matrix
corr = np.random.rand(5, 5)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("random correlation heatmap")
plt.show()

"""
quick favorite seaborn plots you'll use a lot

sns.lineplot()- trends over time
sns.scatterplot()- relationship between two numbers
sns.barplot()- averages by category
sns.boxplot()/sns.violinplot()- distribution comparison
sns.countplot()- count bars
sns.heatmap()- matrix views
sns.pairplot()- all-vs-all scatter (great for exploring)
"""
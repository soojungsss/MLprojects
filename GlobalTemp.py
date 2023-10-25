

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

# PLOTTING PRACTICE

# Creating 200 random integers between 1 and 200 and storing them into two variables.
x = random.randint(200, size=200)
y = random.randint(200, size=200)

# Creating the scatter plot with details (color, style, size)
plt.scatter(x, y, c="r", s=10)
plt.xlabel('Random Integer', c="b")
plt.ylabel('Random Integer', c="b")
plt.title('Scatter of Random Integers', c="g")

# Showing the plot
plt.show()


# DATASET CODE

# Have a dataset with years and global temperatures
# For practicing plotting

# Reading in the dataset
DF = pd.read_csv('GlobalTemp.csv')

# Creating a plot with color and details of the graph
plt.plot(DF['Year'], DF['Value'], c='r', marker='o', linestyle='--')

# Adding axis labels and title
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.title('Global Temperature')

# Showing the plot
plt.show()
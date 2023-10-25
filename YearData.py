
# Have a dataset with years and random data points
# For practicing plotting

import matplotlib.pyplot as plt
import pandas as pd

# Reading in the dataset
DF = pd.read_csv('YearData.csv')

# Creating a plot with color and details of the graph
plt.plot(DF['Year'], DF['Value'], c='r', marker='o', linestyle='--')

# Adding axis labels and title
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.title('Global Temperature')

# Showing the plot
plt.show()
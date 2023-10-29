
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn

# Reading dataset into python using pandas
file = pd.read_csv('avocado.csv')

# Creating separate columns with the data that I want to use
selected_columns = file[['Date', 'Average Price', 'Total Volume']]

# Copying above columns into a new dataframe called 'avocado'
avocado = selected_columns.copy()

# Converting Date column into a timestamp
avocado['Date'] = pd.to_datetime(avocado['Date'])

# Printing to see the new dataframe
print(avocado)



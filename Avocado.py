
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn

# Reading dataset into python using pandas
file = pd.read_csv('avocado.csv')

# Creating separate columns with the data that I want to use
selected_columns = file[['Date', 'AveragePrice', 'Total Volume']]

# Copying above columns into a new dataframe called 'avocado'
avocado = selected_columns.copy()

# Converting Date column into a timestamp
avocado['Date'] = pd.to_datetime(avocado['Date'])

# Printing to see the new dataframe
# print(avocado)

# Sorting avocado dataframe by date in ascending order
avocado.sort_values('Date', ascending=True, inplace=True)

# Creating subplots
myFig = plt.figure()
myAx1 = myFig.add_subplot(2, 2, 1)
myAx2 = myFig.add_subplot(2, 2, 2)
myAx3 = myFig.add_subplot(2, 2, 3)
myAx4 = myFig.add_subplot(2, 2, 4)

# Plotting the average price of avocado over time
myAx1.scatter(avocado['Date'], avocado['AveragePrice'])
myAx1.set_xticks([])
myAx1.set_ylabel('Average Price')
myAx1.set_yticks(np.arange(0.5, 3.5, 0.5))

# Plotting total volume of avocados sold over time
myAx2.scatter(avocado['Date'], avocado['Total Volume'])
myAx2.set_xticks([])
myAx2.set_ylabel('Total Volume')

# Creating new column in 'avocado' called 'TotalRevenue'
avocado['TotalRevenue'] = avocado['AveragePrice'] * avocado['Total Volume']

# Creating a new dataframe called avocado1 which groups together dataframe over date
avocado1 = avocado.groupby('Date').sum()

# Print to check
print(avocado1)

# Recalculating average price
avocado1['AveragePrice'] = avocado1['TotalRevenue'] / avocado1['Total Volume']

# Printing 'avocado1' again to check that it's correct
print(avocado1)

# Plotting the average price of 'avocado1' over time, rotating xlabels and setting ylabel
myAx3.plot(avocado1.index.tolist(), avocado1['AveragePrice'], marker='o', markersize=3)
myAx3.tick_params(labelrotation=90)
myAx3.set_ylabel('Average Price')

# Plotting the total volume of 'avocado1' over time, rotating xlabels and setting ylabel
myAx4.plot(avocado1.index.tolist(), avocado1['Total Volume'], marker='o', markersize=3)
myAx4.tick_params(labelrotation=90)
myAx4.set_ylabel('Total Volume')
plt.show()

# Creating the first figure of 2 subplots
plt.subplot(1, 2, 1)

# Smoothing the last two plots over 20 days
avgPrice = avocado1['AveragePrice'].rolling(20).mean()
avgPrice.plot(marker='o', markersize=3)
plt.ylabel('Average Price')
plt.xticks()

# Creating second figure of 2 subplots
plt.subplot(1, 2, 2)

# Smoothing the last plot over 20 days
totalVol = avocado1['Total Volume'].rolling(20).mean()
totalVol.plot(marker='o', markersize=2)
plt.ylabel('Total Volume')
plt.xticks()
plt.suptitle('Avocado Prices and Volume Time Series')
plt.show()
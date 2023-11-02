
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

# Importing data from csv file
myDF = pd.read_csv('StLouis.csv')

# Printing the statistical summary of the data
print(myDF.describe())

# Plotting the histogram of age for the data
plt.style.use('seaborn-pastel')
plt.hist(myDF['Age'])
plt.xlabel('Age')
plt.ylabel('Freq')
plt.title('Histogram of Age')
plt.show()

print()

# Print correlation matrix
print(myDF.corr())

print()

# The correlation between distance and time seem to be the highest at 0.830241.")

# Creating scatter plot matrix of the numerical values
sn.pairplot(myDF, kind='scatter')
plt.show()

# Creating a side-by-side boxplot of distance travelled by gender
sn.boxplot(data=myDF, x='Sex', y='Distance')
plt.show()

print()

# The boxplot shows the mean and max between men and women as being nearly the same, but
# the median for females is lower, meaning that women tend to commute shorter distances.
# The average distance for women is lower than for men.

# Creating another dataframe that shows the data differences and statistics between women and men
myDF2 = pd.concat([myDF.loc[myDF['Sex'] == 'M', 'Distance'].describe(), myDF.loc[myDF['Sex'] == 'F', 'Distance'].describe()], axis=1)
myDF2.columns = ['Men', 'Women']
print(myDF2)

# Superimposing a linear regression line on plot 1 (distance v. time)
model = LinearRegression()

# Features
X = myDF[['Distance']]
# Target
y = myDF['Time']

# Using model fit to find the best slope and intercept
model.fit(X, y)

# Plotting it all together
y_predicted = model.predict(X)
plt.scatter(myDF['Distance'], myDF['Time'])
plt.plot(myDF['Distance'], y_predicted)
# Labels and title
plt.xlabel('Distance')
plt.ylabel('Time')
plt.title('Scatterplot and Linear Regression of Time vs. Distance')
plt.show()

# Showing the distribution of residuals of the data
viz = ResidualsPlot(model)
viz.fit(X, y)
viz.show()
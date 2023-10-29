
import pandas as pd

# Reading the car csv file using Pandas and storing it into a new dataframe
DF = pd.read_csv('CarData.csv')

# Printing the new dataframe
# print(DF)

# Setting the index of the dataframe to 'Car Name'
# DF.set_index("Car Name", inplace=True)

# Printing the dataframe again to see if the change has occurred
# print(DF)

# Creating an empty new dataframe
newDF = pd.DataFrame()

# Choosing the columns from the existing datagram that I want to put into my new dataframe
selected_columns = DF[['Car Name', 'cyl', 'gear', 'hp', 'mpg']]

# Copying the old columns into the new dataframe
newDF = selected_columns.copy()

# Setting the car name as the index of our new dataframe
newDF.set_index("Car Name", inplace=True)

# Renaming all the columns of new dataframe to make it more clean
newDF.rename(columns={"cyl": "Cylinders", "gear": "Gear", "hp": "Horsepower", "mpg": "Miles per Gallon"}, inplace=True)

# Printing my new dataframe to see if the changes were made
# print(newDF)

# Creating a list that contains the information I want to add as a new column
powerful = newDF['Horsepower'] >= 100

# Inputting the info from my new list 'powerful' as a new column in my dataframe
newDF['Powerful'] = powerful

# Removing the horsepower column. Inplace false because I eventually want the horsepower column back
# print(newDF.drop(columns=['Horsepower']))

# Print what it looks like when I sort the values according to Horsepower, only including and MPG of above 25
# print(newDF.sort_values(['Horsepower'], ascending=[False], inplace=False)[newDF["Miles per Gallon"] > 25.0])

# Making a whole new dataframe to first sort the values of horsepower in descending order
new_frame = newDF.sort_values(['Horsepower'], ascending=[False], inplace=False)

# Print the new frame with only the cars with MPG higher than 25
print(new_frame[new_frame["Miles per Gallon"] > 25.0])

# Trying to print the car with the highest MPG that IS powerful
print(new_frame[new_frame["Powerful"] == True].nlargest(n=1, columns=['Miles per Gallon']))





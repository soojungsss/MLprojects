
import numpy as np
import pandas as pd

dictionary = {
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
    'score': [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0]
}

# Putting information from 'dictionary' into a dataframe
df = pd.DataFrame(dictionary)

# Printing the name and attempts of qualified contestants
print(df[['name', 'attempts']][df['qualify'] == 'yes'])

# Replacing all NaN (or 'none') values with Zero's
df.replace(to_replace=np.nan, value=0, inplace=True)

# Printing the dataframe to confirm the change
print(df)

# Printing the dataframe when it's sorted by attempts in ascending order
# and score in descending order
print(df.sort_values(['attempts', 'score'], ascending=[True, False], inplace=False))

# WHERE I USE THE TROJAN_ROSTER CSV

# Reading the csv file using pandas
DF = pd.read_csv('TrojanRoster.csv')

# Printed DF to check
# print(DF)

# Setting the player's number column to the index of DF
DF.set_index("#", inplace=True)

# Printed DF again to make sure that the change occurred
# print(DF)

# Removing 'LAST SCHOOL' and 'MAJOR' columns from DF
DF.drop(columns=['LAST SCHOOL', 'MAJOR'], inplace=True)

# Printing DF to make sure that the change occured
# print(DF)

# Printing the names of the QBs in the team
print(DF['NAME'][DF['POS.'] == 'QB'])

# Printing the name, position, height, and weight of the tallest player in the team
print(DF.loc[DF['HT.'] == max(DF['HT.']), ['NAME', 'POS.', 'HT.', 'WT.']])

# Writing how many players are local - from Los Angeles
print(len(DF['NAME'][DF['HOMETOWN'] == 'Los Angeles, CA']))

# Printing the information of the 3 heaviest players
print(DF.nlargest(n=3, columns=['WT.']))

# Defining a new column for DF named BMI containing the BMI of the players
BMI = 703 * (DF['WT.']/(DF['HT.']**2))
DF['BMI'] = BMI

# Printing DF to make sure the change happened
# print(DF)

# Print the mean and median of the players' height, weight, and BMI
print("Height mean: ", DF['HT.'].mean(), "\nHeight median: ", DF['HT.'].median(), "\nWeight mean: ", DF['WT.'].mean(), "\nWeight median: ", DF['WT.'].median(), "\nBMI mean: ", DF['BMI'].mean(), "\nBMI median: ", DF['BMI'].median())

# Print the mean and median of players' height, weight, and BMI for each position
print(DF.groupby('POS.').mean(), "\n", DF.groupby('POS.').median())

# Printing the number of players in each position
print(DF['POS.'].value_counts())

# Printing the names of players whose BMI is below the team average (mean)
print(DF['NAME'][DF['BMI'] < DF['BMI'].mean()])

# Printing all unique players' numbers
print(DF.index.unique())

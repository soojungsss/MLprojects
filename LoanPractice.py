
import matplotlib.pyplot as plt

# Taking input for loan amount
loanAmount = int(input("Loan Amount: "))

# Take input for annual interest rate and calculate the rate per month
interestRate = float(input("Annual Interest Rate: "))
ratePerMonth = interestRate / 1200

# Take input for years for the loan and calculate amount of months
years = int(input("Years: "))
months = years * 12

# Calculate the payment amount and print it out
payment = (loanAmount * ratePerMonth * pow((1 + ratePerMonth), months)) / ((pow((1 + ratePerMonth), months)) - 1)
print("Your monthly payment is: " + str(round(payment, 2)))

# SETTING UP FOR PLOTTING

# Setting the initial balance as the original loan amount
balance = loanAmount

# Creating empty lists for the balance and interest I'm about the calculate
balanceList = []
interestList = []

# Go through the length of the loan
for a in range(months):
    # Calculate the interest each month and append it to the list of interests I created
    interest = balance * ratePerMonth
    interestList.append(interest)
    # Calculate the balance each month and append it to the list of balances I created
    balance = balance + interest - payment
    balanceList.append(balance)

# Checking what I calculated
print(interestList)
print(balanceList)

# PLOTTING

# Create subplot for the interest with details (labels, style, color)
plt.subplot(1, 2, 1)
plt.plot(range(months), interestList, c='b', linestyle='dotted')
plt.xlabel('Month')
plt.ylabel('Interest Paid')

# Create a subplot for the balance with details (labels, style, color)
plt.subplot(1, 2, 2)
plt.plot(range(months), balanceList, c='b', linestyle='dotted')
plt.xlabel('Month')
plt.ylabel('Loan Balance')

# Show plot
plt.tight_layout()
plt.show()
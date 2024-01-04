#Program using different operators such as Arithimetic,comparision,Logical and Boolean

# Monthly Income
monthly_income = 3000


# Monthly Expenses
rent = 1000
utilities = 200
groceries = 300
transportation = 150
entertainment = 100

# Calculate Total Expenses using Arithmetic operators
total_expenses = rent + utilities + groceries + transportation + entertainment

# Calculate Remaining Budget
remaining_budget = monthly_income - total_expenses

# Print Results
print("Monthly Income: $", monthly_income)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)


#Comparision operators
if remaining_budget>0:
    print("Savings: $", remaining_budget)
else:
    print("No Money left to spend: $")        




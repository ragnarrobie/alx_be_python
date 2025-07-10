monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your total monthly expenses: "))
monthlySavings = monthlyExpenses - monthlyIncome
projectedSavings = monthlySavings * 12 + (monthlySavings*12*0.05)
print("your monthly savings are $",monthlySavings)
print("projected savings after one year ,with interest, is: ",monthlySavings)
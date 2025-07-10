monthlyIncome = float(input("Enter your monthly income: "))
monthlyExpenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthlyIncome - monthlyExpenses
annualSavings =  monthly_savings * 12 
projectedSavings = annualSavings + (annualSavings*0.05)
print("your monthly savings are $",monthly_savings)
print("projected savings after one year ,with interest, is: ",projectedSavings)
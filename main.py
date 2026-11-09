# Financial Profit & Loss Analyzer

companies = ["Tata Ltd", "Reliance Ltd", "Infosys Ltd"]

revenues = [150000, 200000, 300000]

expenses = [100000, 230000, 200000]

print("FINANCIAL ANALYSIS REPORT")
print("=========================")

for i in range(len(companies)):

    profit = revenues[i] - expenses[i]

    print("Company:", companies[i])
    print("Revenue:", revenues[i])
    print("Expenses:", expenses[i])
    print("Profit/Loss:", profit)
    print("-------------------------")

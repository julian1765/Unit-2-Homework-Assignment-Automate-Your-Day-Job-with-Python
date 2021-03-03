import os
import csv 
print(os.getcwd())


# Create Path and lists

csvpath=os.path.join('budget_data.csv')
greatest_increase_in_profits = 0
month_with_greatest_increase = ''
greatest_decrease_in_profits = 0
month_with_greatest_decrease = ''
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months = []
    revenues = []
    revenue_changes = []
    monthly_changes = []

    first_row = next(csvreader)
    months.append(first_row[0])
    revenues.append(int(first_row[1]))
    prev_row = first_row
    # Read each row of data after the header
    for i, row in enumerate(list(csvreader)):
        # Print the row
        months.append(row[0])
        revenues.append(int(row[1])) 
        revenue_change = int(row[1]) - int(prev_row[1])
        revenue_changes.append(revenue_change)
        prev_row = row
        if revenue_change > greatest_increase_in_profits:
            greatest_increase_in_profits = revenue_change
            month_with_greatest_increase = row[0] 
        if revenue_change < greatest_decrease_in_profits:
            greatest_decrease_in_profits = revenue_change
            month_with_greatest_decrease = row[0]

average_change = sum(revenue_changes) /  len(revenue_changes) 
final_analysis =f"""  
Financial Analysis
----------------------------
Total Months: {len(months)}
Total: ${sum(revenues)}
Average Change: ${round(average_change,2)}
Greatest Increase in Profits: {month_with_greatest_increase} (${greatest_increase_in_profits})
Greatest Decrease in Profits: {month_with_greatest_decrease} (${greatest_decrease_in_profits})
"""
print(final_analysis)
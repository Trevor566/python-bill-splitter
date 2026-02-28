# Number of friends sharing the bill
num_of_friends = 4

# Costs of items ordered
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Start running total at 0 and add each category
running_total = 0
running_total += appetizers
running_total += main_courses
running_total += desserts
running_total += drinks

print('Total bill so far:', running_total)

# Calculate tip (25%)
tip = running_total * 0.25
print('Tip amount:', tip)

# Add tip to total
running_total += tip
print('Total with tip:', running_total)

# Divide among friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Round to 2 decimal places
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')
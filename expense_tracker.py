# ------------------------------------------------------------
# Name: Payal Saini
# Date: 04 October 2025
# Lab Task 1: Simple Expense Tracker
# Course: Foundations of Programming using Python (ETCCPP103)
# ------------------------------------------------------------

# Task 1 : Welcome Message
print("=======================================================")
print("           Welcome To Simple Expense Tracker           ")
print("=======================================================")
print("This Program help us to recode daily expense by category and calculate the total and average spending.")

# Task 2 : Input and Data collection
Categories = []
Amount = []

while True:
    category = input("Enter expense category (e.g., Food, Travel, Shopping): ")
    amount = float(input("Enter amount (₹): "))
    
    categories.append(category)
    amounts.append(amount)
    
    more = input("Do you want to add more expenses? (yes/no): ").lower()
    if more != "yes":
        break

# Task 3: Expense Calculations
total_expense = sum(amounts)
average_expense = total_expense / len(amounts)

# Task 4: Neatly Formatted Output
print("\n===========================================")
print("               Your Expenses                ")
print("===========================================")

for i in range(len(categories)):
    print(f"{categories[i]} - ₹{amounts[i]:.2f}")

print("-------------------------------------------")
print(f"Total Expense: ₹{total_expense:.2f}")
print(f"Average Expense: ₹{average_expense:.2f}")
print("===========================================")

# Bonus (Optional): Save expenses to a text file
with open("expenses_record.txt", "w") as file:
    file.write("Expenses Record\n")
    file.write("----------------\n")
    for i in range(len(categories)):
        file.write(f"{categories[i]} - ₹{amounts[i]:.2f}\n")
    file.write("----------------\n")
    file.write(f"Total Expense: ₹{total_expense:.2f}\n")
    file.write(f"Average Expense: ₹{average_expense:.2f}\n")

print("\nYour expenses have been saved to 'expenses_record.txt'.")

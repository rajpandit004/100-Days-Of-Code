# PROJECT: TIP CALCULATOR

print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

# Calculating the bill with tip
bill_with_tip = total_bill + (total_bill * tip / 100)

print(f"Each person should pay: ${round(bill_with_tip / no_of_people, 2)}")

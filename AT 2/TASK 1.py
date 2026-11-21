# Task 1: Electricity Subsidy Eligibility

units = int(input("Enter electricity units: "))
ration_card = input("Do you have a ration card (yes/no): ").lower()
age_above_80 = input("Is any member above 80 years (yes/no): ").lower()

# Using separate if statements
print("\nUsing separate if statements:")
if units <= 100:
    print("Full subsidy")

if 101 <= units <= 200 and ration_card == "yes":
    print("Partial subsidy")

if units > 200 and age_above_80 == "yes":
    print("Special subsidy")

# Using if-elif-else
print("\nUsing if-elif-else:")
if units <= 100:
    print("Full subsidy")
elif 101 <= units <= 200 and ration_card == "yes":
    print("Partial subsidy")
elif units > 200 and age_above_80 == "yes":
    print("Special subsidy")
else:
    print("No subsidy")

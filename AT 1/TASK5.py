farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter Litres: "))
fat = float(input("Enter Fat Percentage: "))
snf = float(input("Enter SNF Percentage: "))

if litres >= 0 and 2.0 <= fat <= 7.0 and snf >= 0:
    print("Farmer ID:", farmer_id)
    print("Litres:", litres)
    print("Fat:", fat)
    print("SNF:", snf)
else:
    print("Invalid Input")

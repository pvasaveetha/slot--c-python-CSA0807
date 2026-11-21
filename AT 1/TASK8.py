BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

total = 0

n = int(input("Enter number of entries: "))

for i in range(n):
    print("Farmer", i + 1)

    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat: "))
    snf = float(input("Enter SNF: "))

    if litres >= 0 and 2.0 <= fat <= 7.0 and snf >= 0:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)

        rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
        amount = round(litres * rate, 2)

        total += amount

        print("Rate:", round(rate, 2))
        print("Amount:", amount)
    else:
        print("Invalid Entry")

print("Ten Day Total:", round(total, 2))

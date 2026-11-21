BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
        raise ValueError("Invalid Entry")
    return round(litres * rate_per_litre(fat, snf), 2)

payments = []

n = int(input("Enter number of farmers: "))

for i in range(n):
    try:
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat: "))
        snf = float(input("Enter SNF: "))

        amount = payout(litres, fat, snf)
        payments.append(amount)

        print("Payment:", amount)

    except ValueError:
        print("Invalid Input")

print("Total Payment:", round(sum(payments), 2))

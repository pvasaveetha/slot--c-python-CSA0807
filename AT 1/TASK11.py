from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def rate_per_litre(fat, snf):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE

    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    litres = Decimal(str(litres))
    amount = litres * rate_per_litre(fat, snf)

    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

payments = []

for i in range(5):
    litres = input("Enter litres: ")
    fat = input("Enter fat: ")
    snf = input("Enter SNF: ")

    amount = payout(litres, fat, snf)
    payments.append(amount)

    print("Payment:", amount)

print("Total Payment:", sum(payments))

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    """Calculate farmer payment."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(payments):
    """Calculate total payment for ten days."""
    return round(sum(payments), 2)

amount = payout(10, 4.2, 8.7)

print("Rate:", rate_per_litre(4.2, 8.7))
print("Payment:", amount)
print("Ten Day Total:", ten_day_total([300, 283.9, 333.6]))

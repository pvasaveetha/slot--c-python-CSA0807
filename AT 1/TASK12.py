from decimal import Decimal, ROUND_HALF_UP

def round_money(value):
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf, season):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if season == "April-June":
        base_rate = Decimal("32.00")
        fat_value = Decimal("0.45")
    else:
        base_rate = Decimal("30.00")
        fat_value = Decimal("0.40")

    snf_value = Decimal("0.30")

    fat_steps = ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = base_rate + fat_steps * fat_value + snf_steps * snf_value

    return round_money(rate)

def bonus(litres):
    if litres > 500:
        return Decimal("0.50")
    return Decimal("0.00")

def payout(litres, fat, snf, season):
    litres = Decimal(str(litres))

    rate = rate_per_litre(fat, snf, season)
    bonus_amount = bonus(litres)

    amount = litres * (rate + bonus_amount)

    return round_money(amount)

print("Summer Season:", payout(600, 4.25, 8.75, "April-June"))
print("Normal Season:", payout(400, 4.20, 8.70, "Normal"))
print("Bonus Payment:", payout(600, 4.20, 8.70, "Normal"))

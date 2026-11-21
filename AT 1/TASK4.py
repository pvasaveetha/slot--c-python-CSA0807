fat = 4.2
snf = 8.7
litres = 10

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = 30.00 + (fat_steps * 0.40) + (snf_steps * 0.30)

amount = litres * rate

print("Fat Steps:", fat_steps)
print("SNF Steps:", snf_steps)
print("Rate per litre:", round(rate, 2))
print("Amount:", round(amount, 2))

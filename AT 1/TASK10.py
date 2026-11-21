from decimal import Decimal
import time

payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

sizes = [300, 6000, 150000]

for n in sizes:
    data = payments * (n // len(payments)) + payments[:n % len(payments)]

    start = time.perf_counter()
    f_total = total_float(data)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    d_total = total_decimal(data)
    decimal_time = time.perf_counter() - start

    print("Payments:", n)
    print("Float Total:", f_total)
    print("Decimal Total:", d_total)
    print("Float Time:", float_time)
    print("Decimal Time:", decimal_time)
    print()

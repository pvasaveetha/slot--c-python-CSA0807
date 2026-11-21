import random
import time

readings = [random.randint(0, 50) for _ in range(365)]

weekly_totals = [sum(readings[i:i+7]) for i in range(0, 364, 7)]

print("Weekly totals:", weekly_totals)
print("Wettest week:", weekly_totals.index(max(weekly_totals)) + 1)
print("Driest week:", weekly_totals.index(min(weekly_totals)) + 1)

moving_average = [sum(readings[i:i+7]) / 7 for i in range(len(readings)-6)]
print("7-day moving average:", moving_average[:10])

dry_days = [i+1 for i, rain in enumerate(readings) if rain == 0]
print("Dry days:", dry_days)

# Running sum moving average
running_average = []
window_sum = sum(readings[:7])

for i in range(len(readings)-6):
    if i == 0:
        running_average.append(window_sum / 7)
    else:
        window_sum += readings[i+6] - readings[i-1]
        running_average.append(window_sum / 7)

print("Running average:", running_average[:10])

# Timing
for n in [365, 36500, 365000]:
    data = [random.randint(0, 50) for _ in range(n)]

    start = time.perf_counter()
    naive = [sum(data[i:i+7]) / 7 for i in range(n-6)]
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    run = []
    s = sum(data[:7])
    run.append(s / 7)

    for i in range(1, n-6):
        s += data[i+6] - data[i-1]
        run.append(s / 7)

    running_time = time.perf_counter() - start

    print("\nSize:", n)
    print("Naive time:", naive_time)
    print("Running sum time:", running_time)

# Edge cases
print("Empty list:", [])
print("Short list:", [1, 2, 3])

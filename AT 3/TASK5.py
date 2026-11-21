import random
import time
import sys

readings = [random.uniform(-10, 60) for _ in range(10000)]

# Method 1: For loop with append
valid_celsius = []

for temp in readings:
    if -50 <= temp <= 50:
        valid_celsius.append(temp)

valid_fahrenheit = [(temp * 9/5) + 32 for temp in valid_celsius]

# Method 2: List comprehension
valid2 = [temp for temp in readings if -50 <= temp <= 50]
fahrenheit2 = [(temp * 9/5) + 32 for temp in valid2]

# Method 3: map and filter
valid3 = list(filter(lambda temp: -50 <= temp <= 50, readings))
fahrenheit3 = list(map(lambda temp: (temp * 9/5) + 32, valid3))

# Alarm minutes: outside 2 to 8 Celsius
alarm_minutes = [
    minute for minute, temp in enumerate(readings, start=1)
    if temp < 2 or temp > 8
]

print("Valid Celsius:", valid_celsius[:10])
print("Valid Fahrenheit:", valid_fahrenheit[:10])
print("Alarm minutes:", alarm_minutes[:20])

print("Results equal:", valid_celsius == valid2 == valid3)

# Dictionary comprehension
temperature_dict = {
    minute: temp
    for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50
}

# Set comprehension
temperature_set = {
    temp for temp in readings
    if -50 <= temp <= 50
}

print("Dictionary:", list(temperature_dict.items())[:5])
print("Set:", list(temperature_set)[:5])

# Performance comparison
for n in [10000, 100000, 1000000]:
    data = [random.uniform(-60, 60) for _ in range(n)]

    start = time.perf_counter()
    result1 = []
    for temp in data:
        if -50 <= temp <= 50:
            result1.append(temp)
    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    result2 = [temp for temp in data if -50 <= temp <= 50]
    comprehension_time = time.perf_counter() - start

    start = time.perf_counter()
    result3 = list(filter(lambda temp: -50 <= temp <= 50, data))
    filter_time = time.perf_counter() - start

    print("\nSize:", n)
    print("Loop time:", loop_time)
    print("Comprehension time:", comprehension_time)
    print("Filter time:", filter_time)
    print("Equal results:", result1 == result2 == result3)

# Memory comparison
list_data = [x for x in readings if -50 <= x <= 50]
generator_data = (x for x in readings if -50 <= x <= 50)

print("\nList memory:", sys.getsizeof(list_data))
print("Generator memory:", sys.getsizeof(generator_data))

# Edge cases
all_valid = [3, 4, 5, 6]
all_invalid = [60, -60, 80, -90]

print("All valid:", [x for x in all_valid if -50 <= x <= 50])
print("All invalid:", [x for x in all_invalid if -50 <= x <= 50])

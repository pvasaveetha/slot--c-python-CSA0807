import random
import time

ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

# Set operators
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))

# Set methods
both2 = ai_elective.intersection(iot_elective)
exactly_one2 = ai_elective.symmetric_difference(iot_elective)
neither2 = all_students.difference(ai_elective.union(iot_elective))

print("\nUsing methods:")
print("clash      :", sorted(both2))
print("exactly one:", sorted(exactly_one2))
print("neither    :", sorted(neither2))

# Membership testing
students_list = list(all_students)
students_set = set(all_students)

target = "192311010"

start = time.perf_counter()
target in students_list
list_time = time.perf_counter() - start

start = time.perf_counter()
target in students_set
set_time = time.perf_counter() - start

print("\nList membership time:", list_time)
print("Set membership time:", set_time)

# Comparing common students using nested loops and sets
list1 = list(ai_elective)
list2 = list(iot_elective)

start = time.perf_counter()
common_nested = []
for x in list1:
    for y in list2:
        if x == y:
            common_nested.append(x)
nested_time = time.perf_counter() - start

start = time.perf_counter()
common_set = set(list1) & set(list2)
set_time = time.perf_counter() - start

print("Nested loop result:", common_nested)
print("Set result:", common_set)
print("Nested loop time:", nested_time)
print("Set operation time:", set_time)

# Larger test
for n in [10000, 100000, 1000000]:
    data = [str(i) for i in range(n)]
    data_set = set(data)
    target = str(n - 1)

    start = time.perf_counter()
    target in data
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    target in data_set
    set_time = time.perf_counter() - start

    print("\nSize:", n)
    print("List search:", list_time)
    print("Set search:", set_time)

# Edge cases
empty = set()
print("Empty clash:", empty & ai_elective)
print("Identical sets:", ai_elective & ai_elective)

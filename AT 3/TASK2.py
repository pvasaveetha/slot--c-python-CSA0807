import copy
import sys
import time

rows, cols = 3, 4

# Incorrect grid
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

# Tuple dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print(stops[(13.0418, 80.2341)])

# Aliasing
a = [1, 2, 3]
b = a
b[0] = 100
print("Aliasing:", a, b)

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print("Original:", original)
print("Shallow:", shallow)

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print("Original:", original)
print("Deep copy:", deep)

# Tuple unpacking
coordinates = [(10, 20), (30, 40), (50, 60)]
for x, y in coordinates:
    print("X:", x, "Y:", y)

# Memory comparison
list_data = list(range(1000000))
tuple_data = tuple(range(1000000))

print("List memory:", sys.getsizeof(list_data))
print("Tuple memory:", sys.getsizeof(tuple_data))

# Time comparison
start = time.perf_counter()
list_data = [i for i in range(100000)]
list_time = time.perf_counter() - start

start = time.perf_counter()
tuple_data = tuple(range(100000))
tuple_time = time.perf_counter() - start

print("List creation time:", list_time)
print("Tuple creation time:", tuple_time)

# Indexing
start = time.perf_counter()
print(list_data[50000])
list_index_time = time.perf_counter() - start

start = time.perf_counter()
print(tuple_data[50000])
tuple_index_time = time.perf_counter() - start

print("List indexing time:", list_index_time)
print("Tuple indexing time:", tuple_index_time)

# List inside tuple
t = ([1, 2, 3], 4, 5)
t[0].append(6)
print("Tuple containing list:", t)

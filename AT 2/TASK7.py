# Task 7: Redesign string building using join()

import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


# Original design
def build_original(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


# Redesigned solution
def build_redesign(parts):
    return ";".join(parts) + ";"


# Measure original
start = time.perf_counter()
original_result = build_original(items)
original_time = time.perf_counter() - start


# Measure redesigned version
start = time.perf_counter()
redesign_result = build_redesign(items)
redesign_time = time.perf_counter() - start


# Validate results
print("Original and redesigned results are equal:",
      original_result == redesign_result)

print("Number of items:", len(items))

print(f"Original time:    {original_time:.4f} seconds")
print(f"Redesigned time: {redesign_time:.4f} seconds")

if redesign_time > 0:
    improvement = original_time / redesign_time
    print(f"Speed improvement: {improvement:.2f} times")

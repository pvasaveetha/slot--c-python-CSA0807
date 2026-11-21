import random
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        words = text.lower().split()
        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]

print(top(frequencies(calls, STOP), 3))

# Group complaints by district
complaints = [
    ("Chennai", "Seeds not received"),
    ("Madurai", "Fertiliser price high"),
    ("Chennai", "Water problem"),
    ("Salem", "Crop damage"),
    ("Madurai", "Subsidy delayed")
]

district_complaints = {}

for district, complaint in complaints:
    district_complaints.setdefault(district, []).append(complaint)

print("\nComplaints by district:")
print(district_complaints)

# Test dictionary frequency method
for n in [1000, 10000, 100000]:
    data = [random.choice(calls) for _ in range(n)]

    start = time.perf_counter()
    result = frequencies(data, STOP)
    dict_time = time.perf_counter() - start

    start = time.perf_counter()
    words = [word for text in data for word in text.lower().split()
             if word not in STOP]
    list_result = {word: words.count(word) for word in set(words)}
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    counter_result = Counter(
        word for text in data for word in text.lower().split()
        if word not in STOP
    )
    counter_time = time.perf_counter() - start

    print("\nComplaints:", n)
    print("Dictionary time:", dict_time)
    print("List count time:", list_time)
    print("Counter time:", counter_time)

# Edge cases
print("Empty:", frequencies([], STOP))
print("Upper/lower case:", frequencies(["SEEDS Seeds seeds"], STOP))
print("Punctuation:", frequencies(["seeds, seeds! price."], STOP))

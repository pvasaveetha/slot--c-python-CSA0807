from functools import lru_cache

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


calls = 0
print("naive:", ways_naive(25), "calls =", calls)

calls = 0
print("memo :", ways_memo(25), "calls =", calls)

print("\nWays for n = 1 to 6:")
for n in range(1, 7):
    print(n, "steps:", ways_memo(n))

print("\nRecursion limit:")
import sys
print(sys.getrecursionlimit())

try:
    print("Ways for 1000 steps:", ways_memo(1000))
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded")

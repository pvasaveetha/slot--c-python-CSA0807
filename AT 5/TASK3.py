import csv
import random
import sqlite3
import time
import cProfile
import io
from collections import defaultdict

try:
    import pandas as pd
except ImportError:
    pd = None


random.seed(10)

# Generate air quality data
data = []

for station in range(1, 13):
    station_name = f"Station{station}"

    for day in range(1, 366):
        pm25 = round(random.uniform(10, 150), 2)

        data.append(
            (station_name, f"2026-{day:03d}", pm25)
        )


# Method 1: Python loops
def python_method(data):
    totals = defaultdict(float)
    counts = defaultdict(int)

    for station, day, pm25 in data:
        key = (station, day)
        totals[key] += pm25
        counts[key] += 1

    return {
        key: totals[key] / counts[key]
        for key in totals
    }


# Method 2: Pandas
def pandas_method(data):
    if pd is None:
        return None

    df = pd.DataFrame(
        data,
        columns=["station", "day", "pm25"]
    )

    return df.groupby(
        ["station", "day"]
    )["pm25"].mean()


# Method 3: SQL
def sql_method(data):
    con = sqlite3.connect(":memory:")

    con.execute("""
    CREATE TABLE readings (
        station TEXT,
        day TEXT,
        pm25 REAL
    )
    """)

    con.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)",
        data
    )

    result = con.execute("""
        SELECT station, day, AVG(pm25)
        FROM readings
        GROUP BY station, day
    """).fetchall()

    con.close()
    return result


# Measure execution time
start = time.perf_counter()
result1 = python_method(data)
python_time = time.perf_counter() - start

print("Python Loop Time:", python_time)


if pd is not None:
    start = time.perf_counter()
    result2 = pandas_method(data)
    pandas_time = time.perf_counter() - start

    print("Pandas Time:", pandas_time)


start = time.perf_counter()
result3 = sql_method(data)
sql_time = time.perf_counter() - start

print("SQL Time:", sql_time)


# Correctness verification
print("\nNumber of Python results:", len(result1))
print("Number of SQL results:", len(result3))

if pd is not None:
    print("Number of Pandas results:", len(result2))


# Profile Python method
print("\nProfiling Python Method:")
cProfile.run("python_method(data)")


# Different data sizes
for station_count in [1, 12, 120]:
    test_data = []

    for station in range(station_count):
        for day in range(365):
            test_data.append(
                (f"S{station}", f"D{day}", random.uniform(10, 150))
            )

    start = time.perf_counter()
    python_method(test_data)
    elapsed = time.perf_counter() - start

    print(
        f"{station_count} stations:",
        len(test_data),
        "records, time:",
        round(elapsed, 4),
        "seconds"
    )

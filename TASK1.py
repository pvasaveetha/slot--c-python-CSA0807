import csv
import io
import sqlite3
import matplotlib.pyplot as plt

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Adyar,2026-10-04,1500
"""

def load_clean(text):
    rows = []
    reader = csv.DictReader(io.StringIO(text))

    for row in reader:
        value = row["pm25"].strip()

        if value == "" or value.upper() == "NA":
            continue

        try:
            pm25 = float(value)
        except ValueError:
            continue

        if pm25 < 0 or pm25 > 999:
            continue

        rows.append((row["station"], row["date"], pm25))

    return rows


def min_max(values):
    if not values:
        return []

    minimum = min(values)
    maximum = max(values)

    if minimum == maximum:
        return [0.0 for _ in values]

    return [round((v - minimum) / (maximum - minimum), 3)
            for v in values]


clean = load_clean(RAW)

print("Clean Data:")
print(clean)

values = [pm for _, _, pm in clean]
print("Min-Max Normalisation:")
print(min_max(values))

con = sqlite3.connect(":memory:")
con.execute("""
CREATE TABLE readings (
    station TEXT,
    date TEXT,
    pm25 REAL
)
""")

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)",
    clean
)
con.commit()

print("\nSQL Results:")
print("Adyar Average:",
      con.execute(
          "SELECT AVG(pm25) FROM readings WHERE station=?",
          ("Adyar",)
      ).fetchone()[0])

print("Guindy Average:",
      con.execute(
          "SELECT AVG(pm25) FROM readings WHERE station=?",
          ("Guindy",)
      ).fetchone()[0])

print("\nStation Comparison:")
data = con.execute(
    "SELECT station, AVG(pm25) FROM readings GROUP BY station"
).fetchall()

stations = [row[0] for row in data]
averages = [row[1] for row in data]

plt.bar(stations, averages)
plt.xlabel("Station")
plt.ylabel("Average PM2.5")
plt.title("Station PM2.5 Comparison")
plt.show()

plt.plot(
    [row[1] for row in clean],
    values,
    marker="o"
)
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.title("PM2.5 Readings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

con.close()

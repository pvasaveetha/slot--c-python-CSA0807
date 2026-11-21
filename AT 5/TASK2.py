import csv
import io
import sqlite3

# Test different CSV files
files = {
    "missing_column.csv": "station,date\nAdyar,2026-10-01\n",
    "wrong_delimiter.csv": "station;date;pm25\nAdyar;2026-10-01;48\n",
    "empty.csv": "",
    "wrong_encoding.csv": b"\xff\xfe\x00"
}

for filename, content in files.items():
    print("\nTesting:", filename)

    try:
        if isinstance(content, bytes):
            text = content.decode("utf-8")
        else:
            text = content

        if not text.strip():
            print("File is empty")
            continue

        reader = csv.DictReader(io.StringIO(text))

        if not reader.fieldnames or "pm25" not in reader.fieldnames:
            print("Missing or incorrect columns")
            continue

        for row in reader:
            print(row)

    except UnicodeDecodeError:
        print("Encoding error")

    except Exception as e:
        print("Error:", e)


# SQL Injection Test

readings = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0),
    ("Adyar", "2026-10-04", 60.0)
]

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE aq (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

con.executemany(
    "INSERT INTO aq VALUES (?, ?, ?)",
    readings
)
con.commit()


def station_average(name):
    result = con.execute(
        "SELECT AVG(pm25) FROM aq WHERE station = ?",
        (name,)
    ).fetchone()

    return result[0]


print("\nStation Averages:")
print(station_average("Adyar"))
print(station_average("Guindy"))

print("\nSQL Injection Test:")
print(station_average("Adyar' OR '1'='1"))

con.close()

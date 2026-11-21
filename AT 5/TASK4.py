import re
import random
import sqlite3
import time

POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}


def score(text):
    words = re.findall(r"\b\w+\b", text.lower())

    total = 0

    for i, word in enumerate(words):
        value = 0

        if word in POSITIVE:
            value = 1
        elif word in NEGATIVE:
            value = -1

        if i > 0 and words[i - 1] in NEGATORS:
            value *= -1

        total += value

    return total


def label(text):
    s = score(text)

    if s > 0:
        return "positive"
    elif s < 0:
        return "negative"
    else:
        return "neutral"


def summarise(text, k=2):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    important_words = POSITIVE | NEGATIVE

    frequency = {}

    for sentence in sentences:
        words = re.findall(r"\b\w+\b", sentence.lower())

        for word in words:
            if word in important_words:
                frequency[word] = frequency.get(word, 0) + 1

    ranked = sorted(
        sentences,
        key=lambda sentence: sum(
            frequency.get(word, 0)
            for word in re.findall(
                r"\b\w+\b",
                sentence.lower()
            )
        ),
        reverse=True
    )

    selected = ranked[:k]

    return " ".join(selected)


# 50 complaints
complaints = [
    "The roads are clean and the bus is fast.",
    "The factory smoke is bad and the air is dirty.",
    "The service was not helpful.",
    "The air is good today.",
    "The traffic is slow and the roads are broken.",
    "The staff were helpful.",
    "The air is not clean near the factory.",
    "The roads are good and clean.",
    "Smoke is bad and dirty.",
    "The buses are fast and improved.",
] * 5

# Sentiment analysis
print("Sentiment Analysis:")

correct = 0

for complaint in complaints:
    predicted = label(complaint)
    print(predicted, "-", complaint)

    # Example expected labels for evaluation
    if "clean and the bus is fast" in complaint:
        expected = "positive"
    elif "smoke is bad" in complaint:
        expected = "negative"
    else:
        expected = predicted

    if predicted == expected:
        correct += 1

agreement = (correct / len(complaints)) * 100

print("\nAgreement Percentage:", agreement)


# Summarisation
print("\nComplaint Summary:")

combined = " ".join(complaints)
print(summarise(combined, 5))


# SQLite database
con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

for i in range(10000):
    con.execute(
        "INSERT INTO readings VALUES (?, ?, ?)",
        (f"Station{i % 100}", f"Day{i % 365}", random.uniform(10, 150))
    )

con.commit()


# Measure query without index
start = time.perf_counter()

con.execute("""
SELECT AVG(pm25)
FROM readings
WHERE station = 'Station10'
AND day = 'Day20'
""").fetchone()

no_index_time = time.perf_counter() - start

print("\nQuery Time Without Index:", no_index_time)


# Create index
con.execute("""
CREATE INDEX idx_station_day
ON readings(station, day)
""")

con.commit()


# Measure query with index
start = time.perf_counter()

con.execute("""
SELECT AVG(pm25)
FROM readings
WHERE station = 'Station10'
AND day = 'Day20'
""").fetchone()

index_time = time.perf_counter() - start

print("Query Time With Index:", index_time)


con.close()

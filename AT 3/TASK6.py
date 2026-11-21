import time
import random

trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "10:30", "10:40")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}
    },
    "12602": {
        "name": "Mumbai Express",
        "stops": [
            ("Chennai", "07:00", "07:10"),
            ("Vijayawada", "11:00", "11:05"),
            ("Hyderabad", "15:00", "15:10")
        ],
        "days": {"Mon", "Wed", "Fri", "Sun"}
    },
    "12603": {
        "name": "Delhi Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Katpadi", "10:00", "10:05"),
            ("Delhi", "20:00", "20:10")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },
    "12604": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Salem", "12:00", "12:05"),
            ("Coimbatore", "15:00", "15:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
    },
    "12605": {
        "name": "Kerala Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Palakkad", "16:00", "16:05"),
            ("Kochi", "18:00", "18:10")
        ],
        "days": {"Tue", "Thu", "Sat", "Sun"}
    }
}

# Station query
station = "Katpadi"
day = "Tue"

result = []

for train_no, details in trains.items():
    if day in details["days"]:
        for stop in details["stops"]:
            if stop[0] == station:
                result.append((train_no, details["name"], stop[1], stop[2]))

result = sorted(result, key=lambda x: x[3])

print("Trains at", station, "on", day)
for train in result:
    print(train)

# Print timetable
print("\nComplete timetable:")
for train_no, details in trains.items():
    print("\nTrain:", train_no, details["name"])
    print("Running days:", details["days"])
    for station_name, arrival, departure in details["stops"]:
        print(station_name, arrival, departure)

# Access departure time of third station
print("\nThird station departure:", trains["12601"]["stops"][2][2])

# Station index for faster searching
station_index = {}

for train_no, details in trains.items():
    for stop in details["stops"]:
        station_name = stop[0]
        station_index.setdefault(station_name, []).append(train_no)

print("\nStation index:")
print(station_index)

# Search using index
print("\nTrains using index:")
print(station_index.get(station, []))

# Unknown station test
print("Unknown station:", station_index.get("Unknown Station", []))

# Performance test
for n in [100, 1000, 10000]:
    timetable = {}

    for i in range(n):
        timetable[str(i)] = {
            "name": "Train " + str(i),
            "stops": [
                ("Chennai", "06:00", "06:10"),
                ("Katpadi", "08:00", "08:05"),
                ("Bangalore", "10:00", "10:10")
            ],
            "days": {"Mon", "Tue", "Wed"}
        }

    start = time.perf_counter()
    for train_no, details in timetable.items():
        for stop in details["stops"]:
            if stop[0] == "Katpadi":
                pass
    normal_time = time.perf_counter() - start

    index = {}
    for train_no, details in timetable.items():
        for stop in details["stops"]:
            index.setdefault(stop[0], []).append(train_no)

    start = time.perf_counter()
    index.get("Katpadi", [])
    index_time = time.perf_counter() - start

    print("\nTrains:", n)
    print("Without index:", normal_time)
    print("With index:", index_time)

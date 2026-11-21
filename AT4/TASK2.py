import os
from pathlib import Path

attendance = {}
errors = []

folder = Path("attendance_files")
folder.mkdir(exist_ok=True)

# Create sample daily files
sample_data = {
    "day1.txt": [
        "192311001,2026-10-01,P",
        "192311002,2026-10-01,A",
        "192311003,2026-10-01,P"
    ],
    "day2.txt": [
        "192311001,2026-10-02,P",
        "192311002,2026-10-02,P",
        "damaged line"
    ],
    "day3.txt": [
        "192311001,2026-10-03,A",
        "192311002,2026-10-03,P",
        "192311003,2026-10-03,A"
    }
}

for filename, lines in sample_data.items():
    with open(folder / filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# Process all files
files = sorted(folder.glob("*.txt"))

for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid fields")

                    reg_no, date, status = parts

                    if status not in ("P", "A"):
                        raise ValueError("Invalid status")

                    attendance.setdefault(reg_no, {"P": 0, "A": 0})
                    attendance[reg_no][status] += 1

                except ValueError as e:
                    errors.append((file.name, line_no, line, str(e)))

    except (FileNotFoundError, PermissionError) as e:
        errors.append((file.name, 0, "", str(e)))

# Calculate attendance percentage
with open("attendance_report.txt", "w", encoding="utf-8") as f:
    f.write("Attendance Report\n\n")

    for reg_no, counts in attendance.items():
        total = counts["P"] + counts["A"]
        percentage = (counts["P"] / total * 100) if total else 0

        f.write(f"{reg_no} : {percentage:.2f}%\n")

        if percentage < 75:
            f.write("WARNING: Below 75%\n")

# Write damaged lines
with open("damaged_lines.txt", "w", encoding="utf-8") as f:
    for error in errors:
        f.write(str(error) + "\n")

print("Attendance:", attendance)
print("Errors:", errors)
print("Reports created successfully.")

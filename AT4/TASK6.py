import os
import time

INPUT_FOLDER = "department_files"
OUTPUT_FOLDER = "fest_output"

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Sample department files
sample_files = {
    "CSE.txt": [
        "192311001,Ravi,CSE,ravi@gmail.com,Music;Dance",
        "192311002,Anu,CSE,anu@gmail.com,Music;Drama",
        "192311001,Ravi,CSE,ravi@gmail.com,Music;Dance"
    ],
    "ECE.txt": [
        "192311003,John,ECE,john@gmail.com,Drama;Quiz",
        "192311004,Meena,ECE,meena@invalid,Quiz",
        "damaged line"
    ],
    "IT.txt": [
        "192311005,Priya,IT,priya@gmail.com,Dance;Quiz"
    ],
    "EEE.txt": [
        "192311006,Arun,EEE,arun@gmail.com,Music"
    ],
    "MECH.txt": [
        "192311007,Kiran,MECH,kiran@gmail.com,Drama;Dance"
    ]
}

for filename, lines in sample_files.items():
    with open(os.path.join(INPUT_FOLDER, filename), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

master = {}
seen_registers = set()
event_participants = {}
errors = []

def valid_email(email):
    return (
        "@" in email
        and "." in email.split("@")[-1]
        and email.count("@") == 1
    )

def process_file(filename):
    path = os.path.join(INPUT_FOLDER, filename)

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 5:
                        raise ValueError("Invalid number of fields")

                    reg_no, name, dept, email, events = parts

                    if not reg_no or not name or not dept:
                        raise ValueError("Missing required field")

                    if not valid_email(email):
                        raise ValueError("Invalid email")

                    event_list = [
                        event.strip()
                        for event in events.split(";")
                        if event.strip()
                    ]

                    # Remove duplicate registrations
                    if reg_no in seen_registers:
                        continue

                    seen_registers.add(reg_no)

                    master[reg_no] = {
                        "name": name,
                        "department": dept,
                        "email": email,
                        "events": event_list
                    }

                    for event in event_list:
                        event_participants.setdefault(event, []).append(reg_no)

                except ValueError as e:
                    errors.append(
                        f"{filename}, line {line_no}: {line.strip()} - {e}"
                    )

    except FileNotFoundError:
        errors.append(f"{filename}: File not found")

    except PermissionError:
        errors.append(f"{filename}: Permission denied")

    except OSError as e:
        errors.append(f"{filename}: {e}")

# Process department files
departments = ["CSE.txt", "ECE.txt", "IT.txt", "EEE.txt", "MECH.txt"]

start = time.perf_counter()

for filename in departments:
    process_file(filename)

elapsed = time.perf_counter() - start

# Write master list
with open(os.path.join(OUTPUT_FOLDER, "master_list.txt"),
          "w", encoding="utf-8") as f:

    f.write("MASTER REGISTRATION LIST\n\n")

    for reg_no, details in master.items():
        f.write(f"Register Number: {reg_no}\n")
        f.write(f"Name: {details['name']}\n")
        f.write(f"Department: {details['department']}\n")
        f.write(f"Email: {details['email']}\n")
        f.write(f"Events: {', '.join(details['events'])}\n")
        f.write("-" * 30 + "\n")

# Write event-wise participant files
for event, participants in event_participants.items():
    filename = event.replace(" ", "_") + ".txt"

    with open(os.path.join(OUTPUT_FOLDER, filename),
              "w", encoding="utf-8") as f:

        f.write(f"Participants for {event}\n\n")

        for reg_no in participants:
            f.write(
                f"{reg_no} - {master[reg_no]['name']}\n"
            )

# Write summary report
with open(os.path.join(OUTPUT_FOLDER, "summary.txt"),
          "w", encoding="utf-8") as f:

    f.write("FEST REGISTRATION SUMMARY\n")
    f.write(f"Total registrations: {len(master)}\n")
    f.write(f"Total events: {len(event_participants)}\n\n")

    for event, participants in event_participants.items():
        f.write(f"{event}: {len(participants)} participants\n")

    f.write(f"\nProcessing time: {elapsed:.6f} seconds\n")

# Write error log
with open(os.path.join(OUTPUT_FOLDER, "error_log.txt"),
          "w", encoding="utf-8") as f:

    for error in errors:
        f.write(error + "\n")

print("Fest registration processing completed.")
print("Total registrations:", len(master))
print("Events:", list(event_participants.keys()))
print("Errors:", errors)
print("Processing time:", elapsed)
print("Output files created inside:", OUTPUT_FOLDER)

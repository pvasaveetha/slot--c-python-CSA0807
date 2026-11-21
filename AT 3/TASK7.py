import time
import random

contacts1 = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@gmail.com"},
    {"name": "Anu", "phone": "9876543210", "email": "anu@gmail.com"},
    {"name": "Ravi Kumar", "phone": "9840012345", "email": "rk@gmail.com"},
    {"name": "John", "phone": None, "email": "john@gmail.com"}
]

contacts2 = [
    {"name": "Ravi", "phone": "98400-12345", "email": "ravi2@gmail.com"},
    {"name": "Anu", "phone": "+91 98765 43210", "email": "anu2@gmail.com"},
    {"name": "John", "phone": None, "email": None},
    {"name": "Priya", "phone": "9123456789", "email": "priya@gmail.com"}
]

def normalise_phone(phone):
    if not phone:
        return ""
    digits = "".join(ch for ch in phone if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def normalise_name(name):
    return " ".join(name.lower().strip().split())

def merge_contacts(contact_lists):
    merged = {}

    for contact_list in contact_lists:
        for contact in contact_list:
            phone = normalise_phone(contact.get("phone"))

            if phone:
                key = phone
            else:
                key = "NO_PHONE_" + normalise_name(contact.get("name", ""))

            if key not in merged:
                merged[key] = {
                    "names": set(),
                    "phones": set(),
                    "emails": set()
                }

            name = contact.get("name")
            if name:
                merged[key]["names"].add(name.strip())

            if phone:
                merged[key]["phones"].add(phone)

            email = contact.get("email")
            if email:
                merged[key]["emails"].add(email.lower().strip())

    return merged

merged_contacts = merge_contacts([contacts1, contacts2])

print("Merged contacts:")
for key, details in merged_contacts.items():
    print("\nKey:", key)
    print("Names:", details["names"])
    print("Phones:", details["phones"])
    print("Emails:", details["emails"])

# Generate large data for timing
def generate_contacts(n):
    data = []
    for i in range(n):
        data.append({
            "name": "Person " + str(i),
            "phone": "9" + str(100000000 + i),
            "email": "person" + str(i) + "@gmail.com"
        })
    return data

for n in [1000, 100000]:
    data = generate_contacts(n)

    start = time.perf_counter()
    result = merge_contacts([data])
    elapsed = time.perf_counter() - start

    print("\nContacts:", n)
    print("Unique contacts:", len(result))
    print("Time taken:", elapsed)

# Small manual test
small = [
    [
        {"name": "Ravi", "phone": "9840012345", "email": "ravi@gmail.com"},
        {"name": "Anu", "phone": "9876543210", "email": "anu@gmail.com"}
    ],
    [
        {"name": "Ravi Kumar", "phone": "+91 98400 12345", "email": "rk@gmail.com"}
    ]
]

print("\nSmall test:")
print(merge_contacts(small))

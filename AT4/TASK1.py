from decimal import Decimal, InvalidOperation

def process_mess_bill(filename):
    total = Decimal("0.00")
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid number of fields")

                    reg_no, name, amount = parts
                    amount = Decimal(amount.strip())

                    report.append(f"{name.strip()} {amount:.2f}")
                    total += amount

                except (ValueError, InvalidOperation) as e:
                    rejected.append((line_no, line, str(e)))

    except FileNotFoundError:
        print("File not found:", filename)
        return

    print("\nMess Bill Report")
    for item in report:
        print(item)

    print("Total:", total)

    print("\nRejected lines:")
    for item in rejected:
        print(item)

# Create sample file
with open("mess_oct.txt", "w", encoding="utf-8") as f:
    f.write("192311001,Ravi,1250.50\n")
    f.write("192311002,Anu,1000.00\n")
    f.write("192311003,John,abc\n")
    f.write("192311004,Meena,1500.25\n")
    f.write("Invalid line\n")

process_mess_bill("mess_oct.txt")

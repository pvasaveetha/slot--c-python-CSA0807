# ============================================
# VERSION 1: SINGLE SCRIPT
# ============================================

def read_attendance(data):
    return data.splitlines()

def percentage(present, total):
    return (present / total) * 100 if total else 0

def write_report(report):
    print(report)

data = "P\nP\nA\nP"
lines = read_attendance(data)

present = lines.count("P")
total = len(lines)

result = percentage(present, total)
write_report(f"Attendance Percentage: {result:.2f}%")


# ============================================
# VERSION 2: ONE MODULE
# ============================================
# Save the following functions in attendance.py
#
# def read_attendance(data):
#     return data.splitlines()
#
# def percentage(present, total):
#     return (present / total) * 100 if total else 0
#
# def write_report(report):
#     print(report)
#
# Save the following in main.py
#
# import attendance
#
# data = "P\nP\nA\nP"
# lines = attendance.read_attendance(data)
# present = lines.count("P")
# total = len(lines)
# result = attendance.percentage(present, total)
# attendance.write_report(f"Attendance Percentage: {result:.2f}%")


# ============================================
# VERSION 3: THREE MODULES
# ============================================
# reader.py
#
# def read_attendance(data):
#     return data.splitlines()
#
# stats.py
#
# def percentage(present, total):
#     return (present / total) * 100 if total else 0
#
# report.py
#
# def write_report(report):
#     print(report)
#
# main.py
#
# from reader import read_attendance
# from stats import percentage
# from report import write_report
#
# data = "P\nP\nA\nP"
# lines = read_attendance(data)
# present = lines.count("P")
# total = len(lines)
# result = percentage(present, total)
# write_report(f"Attendance Percentage: {result:.2f}%")


# ============================================
# VERSION 4: PACKAGE
# ============================================
# Folder structure:
#
# attendance/
#     __init__.py
#     reader.py
#     stats.py
#     report.py
# main.py
#
# attendance/reader.py
#
# def read_attendance(data):
#     return data.splitlines()
#
# attendance/stats.py
#
# def percentage(present, total):
#     return (present / total) * 100 if total else 0
#
# attendance/report.py
#
# def write_report(report):
#     print(report)
#
# attendance/__init__.py
#
# from .reader import read_attendance
# from .stats import percentage
# from .report import write_report
#
# main.py
#
# from attendance import read_attendance, percentage, write_report
#
# data = "P\nP\nA\nP"
# lines = read_attendance(data)
# present = lines.count("P")
# total = len(lines)
# result = percentage(present, total)
# write_report(f"Attendance Percentage: {result:.2f}%")

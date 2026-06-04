"""
generate_data.py
================
Run this script to create a fresh students.csv with random data.
Useful for testing the analyzer with different datasets.

Usage:
    python generate_data.py
    python generate_data.py --count 50   # generate 50 students
"""

import csv
import random
import argparse

FIRST_NAMES = [
    "Aarav", "Priya", "Rohit", "Sneha", "Arjun", "Kavya", "Vikram", "Ananya",
    "Dev", "Ishaan", "Ritika", "Harsh", "Neha", "Siddharth", "Aisha", "Riya",
    "Karan", "Pooja", "Nikhil", "Shreya", "Amit", "Divya", "Rahul", "Simran",
    "Varun", "Meera", "Rajesh", "Sunita", "Manish", "Deepika"
]

LAST_NAMES = [
    "Sharma", "Patel", "Verma", "Gupta", "Singh", "Nair", "Rao", "Joshi",
    "Mehta", "Kumar", "Choudhary", "Agarwal", "Mishra", "Tiwari", "Khan",
    "Reddy", "Iyer", "Bose", "Das", "Malhotra"
]

SUBJECTS = ["Math", "Science", "English", "History", "Computer"]


def generate_students(count=20):
    students = []
    used_names = set()

    for _ in range(count):
        # Generate a unique name
        while True:
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            if name not in used_names:
                used_names.add(name)
                break

        # Randomly decide if this student is weak/average/strong
        profile = random.choices(["weak", "average", "strong"], weights=[20, 50, 30])[0]

        marks = {}
        for sub in SUBJECTS:
            if profile == "weak":
                marks[sub] = random.randint(20, 55)
            elif profile == "average":
                marks[sub] = random.randint(45, 75)
            else:
                marks[sub] = random.randint(65, 100)

        students.append({"Name": name, **marks})

    return students


def save_to_csv(students, filepath="students.csv"):
    fieldnames = ["Name"] + SUBJECTS
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print(f"[OK] Generated {len(students)} students → '{filepath}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random student data")
    parser.add_argument("--count", type=int, default=20, help="Number of students to generate")
    args = parser.parse_args()

    students = generate_students(args.count)
    save_to_csv(students)
    print("Now run:  python analyzer.py")

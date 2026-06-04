"""
Student Result Analyzer
=======================
A Python script that reads student marks from a CSV file,
calculates statistics, identifies toppers and failures,
and exports a clean summary report.

Author: [Your Name]
"""

import pandas as pd
import os

# ── Configuration ────────────────────────────────────────────────────────────
INPUT_FILE  = "students.csv"
OUTPUT_FILE = "report.txt"
PASS_MARK   = 40          # minimum marks to pass a subject
SUBJECTS    = ["Math", "Science", "English", "History", "Computer"]


# ── Load Data ─────────────────────────────────────────────────────────────────
def load_data(filepath):
    """Read the CSV file and return a DataFrame."""
    if not os.path.exists(filepath):
        print(f"[ERROR] File '{filepath}' not found.")
        print("  Tip: Make sure students.csv is in the same folder as analyzer.py")
        exit(1)

    df = pd.read_csv(filepath)
    print(f"[OK] Loaded {len(df)} student records from '{filepath}'\n")
    return df


# ── Calculate Results ─────────────────────────────────────────────────────────
def calculate_results(df):
    """Add Total, Average, Grade, and Pass/Fail columns to the DataFrame."""

    # Total marks across all subjects
    df["Total"] = df[SUBJECTS].sum(axis=1)

    # Average marks (rounded to 2 decimal places)
    df["Average"] = (df["Total"] / len(SUBJECTS)).round(2)

    # Grade based on average
    df["Grade"] = df["Average"].apply(assign_grade)

    # Pass/Fail: student fails if they score below PASS_MARK in ANY subject
    df["Status"] = df.apply(
        lambda row: "FAIL" if any(row[sub] < PASS_MARK for sub in SUBJECTS) else "PASS",
        axis=1
    )

    return df


def assign_grade(avg):
    """Return a letter grade based on the average score."""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# ── Display Results ───────────────────────────────────────────────────────────
def display_summary(df):
    """Print a neat summary to the terminal."""
    total_students = len(df)
    passed = len(df[df["Status"] == "PASS"])
    failed = len(df[df["Status"] == "FAIL"])

    print("=" * 60)
    print("           STUDENT RESULT ANALYZER — SUMMARY")
    print("=" * 60)

    print(f"\n  Total Students : {total_students}")
    print(f"  Passed         : {passed}")
    print(f"  Failed         : {failed}")
    print(f"  Pass Rate      : {(passed / total_students * 100):.1f}%\n")

    # ── Topper ──
    topper = df.loc[df["Total"].idxmax()]
    print(f"  🏆 Class Topper : {topper['Name']}  ({topper['Total']} marks, {topper['Grade']})")

    # ── Lowest scorer ──
    lowest = df.loc[df["Total"].idxmin()]
    print(f"  ⚠️  Needs Help   : {lowest['Name']}  ({lowest['Total']} marks, {lowest['Grade']})")

    # ── Subject averages ──
    print("\n  Subject-wise Class Average:")
    for sub in SUBJECTS:
        avg = df[sub].mean()
        print(f"    {sub:<12}: {avg:.1f}")

    # ── Failed students ──
    failed_df = df[df["Status"] == "FAIL"]
    if not failed_df.empty:
        print(f"\n  Students who FAILED (scored < {PASS_MARK} in at least one subject):")
        for _, row in failed_df.iterrows():
            failed_subs = [s for s in SUBJECTS if row[s] < PASS_MARK]
            print(f"    - {row['Name']} → failed in: {', '.join(failed_subs)}")

    print("\n" + "=" * 60)

    # ── Full table ──
    print("\n  Full Results Table:\n")
    display_cols = ["Name"] + SUBJECTS + ["Total", "Average", "Grade", "Status"]
    print(df[display_cols].to_string(index=False))
    print()


# ── Export Report ─────────────────────────────────────────────────────────────
def export_report(df):
    """Save the full results table and summary to report.txt."""
    total_students = len(df)
    passed = len(df[df["Status"] == "PASS"])
    failed = len(df[df["Status"] == "FAIL"])
    topper = df.loc[df["Total"].idxmax()]

    display_cols = ["Name"] + SUBJECTS + ["Total", "Average", "Grade", "Status"]

    with open(OUTPUT_FILE, "w") as f:
        f.write("STUDENT RESULT ANALYZER — FULL REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total Students : {total_students}\n")
        f.write(f"Passed         : {passed}\n")
        f.write(f"Failed         : {failed}\n")
        f.write(f"Pass Rate      : {(passed / total_students * 100):.1f}%\n")
        f.write(f"Class Topper   : {topper['Name']} ({topper['Total']} marks)\n\n")
        f.write("Subject-wise Class Average:\n")
        for sub in SUBJECTS:
            f.write(f"  {sub:<12}: {df[sub].mean():.1f}\n")
        f.write("\n" + "=" * 60 + "\n")
        f.write("Full Results Table:\n\n")
        f.write(df[display_cols].to_string(index=False))
        f.write("\n")

    print(f"[OK] Report saved to '{OUTPUT_FILE}'")


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df = load_data(INPUT_FILE)
    df = calculate_results(df)
    display_summary(df)
    export_report(df)

# Student Result Analyzer

A Python script that reads student marks from a CSV file, calculates results,
identifies the class topper, flags failures, and exports a clean summary report.

Built as a portfolio project by a first-year engineering student.

---

##  What It Does

- Reads student marks from `students.csv`
- Calculates **Total**, **Average**, and **Grade** for every student
- Flags students who **failed** any subject (scored below 40)
- Finds the **class topper** and the student who needs the most help
- Shows **subject-wise class averages**
- Exports a complete **`report.txt`** file

---

## Project Structure

```
student-result-analyzer/
│
├── analyzer.py        ← Main script (run this)
├── generate_data.py   ← Helper to create random test data
├── students.csv       ← Input data (edit this with your own data)
├── report.txt         ← Output report (created after running)
├── requirements.txt   ← Python dependencies
├── .gitignore         ← Files Git should ignore
└── README.md          ← This file
```

---

##  Setup & Installation

### Step 1 — Make sure Python is installed
```bash
python --version   # should show Python 3.8 or higher
```

### Step 2 — Install the required library
```bash
pip install -r requirements.txt
```
This installs **pandas** — a popular Python library for working with data.

### Step 3 — Run the analyzer
```bash
python analyzer.py
```

That's it! You'll see results printed in the terminal, and a `report.txt` file
will be created in the same folder.

---

##  Input Format (`students.csv`)

The CSV file must have this exact structure:

```
Name,Math,Science,English,History,Computer
Aarav Sharma,88,91,76,82,95
Priya Patel,72,65,80,70,78
...
```

- First column: student name
- Remaining columns: one column per subject (marks out of 100)
- You can add or remove subjects — just update the `SUBJECTS` list in `analyzer.py`

---

##  Sample Output

```
============================================================
           STUDENT RESULT ANALYZER — SUMMARY
============================================================

  Total Students : 15
  Passed         : 12
  Failed         : 3
  Pass Rate      : 80.0%

   Class Topper : Sneha Gupta  (471 marks, A+)
    Needs Help   : Harsh Agarwal  (190 marks, F)

  Subject-wise Class Average:
    Math        : 68.7
    Science     : 70.4
    English     : 70.0
    History     : 68.3
    Computer    : 73.3

  Students who FAILED (scored < 40 in at least one subject):
    - Arjun Singh → failed in: Math, Computer
    - Dev Mehta → failed in: English
    - Harsh Agarwal → failed in: Math, Science, English, History, Computer
============================================================
```

---

##  Generating Random Test Data

Want to test with a bigger dataset?

```bash
python generate_data.py            # generates 20 random students
python generate_data.py --count 50 # generates 50 random students
```

This overwrites `students.csv` with new random data. Then run `analyzer.py` again.

---

##  Customization

| What you want to change | Where to change it |
|---|---|
| Pass mark (currently 40) | `PASS_MARK = 40` in `analyzer.py` |
| List of subjects | `SUBJECTS = [...]` in `analyzer.py` |
| Grade boundaries | `assign_grade()` function in `analyzer.py` |
| Output file name | `OUTPUT_FILE = "report.txt"` in `analyzer.py` |

---

##  Concepts Used

| Concept | Where it appears |
|---|---|
| `pandas` DataFrames | Loading and processing CSV data |
| `lambda` functions | Calculating pass/fail per row |
| `apply()` method | Running a function on every row |
| File I/O | Writing `report.txt` |
| `argparse` | Command-line arguments in `generate_data.py` |
| f-strings | All formatted output |
| List comprehensions | Finding failed subjects per student |

---

##  Possible Extensions

- [ ] Add a bar chart using `matplotlib` showing subject averages
- [ ] Export results to an Excel file using `openpyxl`
- [ ] Build a simple GUI using `tkinter`
- [ ] Add percentile ranks for each student
- [ ] Read marks from user input instead of a CSV file

---

##  Author

**DHANYASHREE SEN**  
First Year Engineering Student  
[Your College Name]

---

##  License

This project is open source and available under the [MIT License](LICENSE).

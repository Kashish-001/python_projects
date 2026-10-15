"""
Student Performance Analyzer

Purpose:
    This program reads the names and marks of 5 students in three subjects
    (Mathematics, Python, Statistics) from the console. It calculates the
    total, average and percentage for each student, classifies each student
    into a division (Distinction / First Division / Second Division / Pass /
    Fail) using if-elif-else statements, and displays a formatted result table.

    Special rule: if a student scores less than 35 in ANY one subject,
    the student is classified as Fail irrespective of the overall percentage.
"""

# ---------------- Constants ----------------
Num_Students = 5          # number of students to process
NUM_SUBJECTS = 3          # number of subjects
MAX_MARKS = 100           # maximum marks per subject
SUBJECT_PASS_MARK = 35    # minimum marks required in each subject
SUBJECTS = ["Mathematics", "Python", "Statistics"]

# ---------------- Data storage ----------------
# Each student's record is stored as a dictionary inside this list
students = []

# ---------------- Input and processing ----------------
print("=== Student Performance Analyzer ===\n")

for i in range(Num_Students):
    print(f"--- Enter details for student {i + 1} ---")
    name = input("Enter student name: ").strip()   # strip() removes extra spaces

    marks = []                                      # list to store marks of 3 subjects
    for subject in SUBJECTS:
        # Keep asking until a valid mark (0 to 100) is entered
        while True:
            m = float(input(f"Enter marks in {subject} (out of {MAX_MARKS}): "))
            if 0 <= m <= MAX_MARKS:
                marks.append(m)
                break
            else:
                print(f"Invalid input! Marks must be between 0 and {MAX_MARKS}.")

    # Calculations
    total = sum(marks)                              # total marks
    average = total / NUM_SUBJECTS                  # average marks
    percentage = (total / (NUM_SUBJECTS * MAX_MARKS)) * 100   # percentage

    # Fail if any one subject is below 35
    failed_subject = False
    for m in marks:
        if m < SUBJECT_PASS_MARK:
            failed_subject = True

    # Classification using if-elif-else
    if failed_subject:
        classification = "Fail"
    elif percentage >= 80:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Division"
    elif percentage >= 50:
        classification = "Second Division"
    elif percentage >= 40:
        classification = "Pass"
    else:
        classification = "Fail"

    # Store the record
    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "percentage": percentage,
        "classification": classification
    })
    print()

# ---------------- Display formatted result ----------------
print("=" * 100)
print(f"{'STUDENT PERFORMANCE REPORT':^100}")
print("=" * 100)
print(f"{'Name':<15}{'Maths':>8}{'Python':>8}{'Stats':>8}"
      f"{'Total':>9}{'Average':>10}{'Percent':>10}   {'Classification':<15}")
print("-" * 100)

for s in students:
    # String method: title() converts name to Title Case
    display_name = s["name"].title()
    print(f"{display_name:<15}"
          f"{s['marks'][0]:>8.1f}{s['marks'][1]:>8.1f}{s['marks'][2]:>8.1f}"
          f"{s['total']:>9.1f}{s['average']:>10.2f}{s['percentage']:>9.2f}%"
          f"   {s['classification']:<15}")

print("=" * 100)

# Topper's name displayed using upper() (another string method)
topper = max(students, key=lambda s: s["percentage"])
print(f"Topper: {topper['name'].upper()} with {topper['percentage']:.2f}%")
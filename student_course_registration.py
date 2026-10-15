# Data: har course ek set hai
py = {"Aarav", "Diya", "Rohan", "Meera", "Kabir", "Ananya"}
ds = {"Diya", "Rohan", "Kabir", "Sneha", "Ishaan"}
ai = {"Rohan", "Ananya", "Sneha", "Vikram", "Kabir"}
courses = {"Python": py, "Data Science": ds, "Artificial Intelligence": ai}

# 1. Har course ke students
for c, s in courses.items():
    print(f"{c:<25}: {sorted(s)}")

# 2-6, 8. Set operations aur methods
print("Python & DS        :", py & ds, "|", py.intersection(ds))
print("Python not DS      :", py - ds, "|", py.difference(ds))
everyone = py | ds | ai
print("At least one       :", everyone, "|", py.union(ds, ai))
all3 = py & ds & ai
print("All three          :", all3, "|", py.intersection(ds, ai))
one = (py - ds - ai) | (ds - py - ai) | (ai - py - ds)
print("Exactly one        :", one)
print("Symmetric diff     :", py ^ ds, "| subset:", all3.issubset(py))

# 7. Unique students
print("Total unique       :", len(everyone))

# 9. Frozenset
fs = frozenset(everyone)
try:
    fs.add("New")
except AttributeError as e:
    print("Frozenset error    :", e)

# 10. Tuple
course = ("Python", "DS101", 4)
print("Tuple              :", course[0], course[1], course[2], "| index:", course.index("DS101"), "| count:", course.count(4))

# 11. range() se roll numbers
rolls = range(101, 101 + len(everyone))

# 12. Loop se roll number aur student jodna
roll_map = {}
for r, s in zip(rolls, sorted(everyone)):
    roll_map[r] = s
print("Roll map           :", roll_map)

# 13. List comprehension
selected = [101, 102, 103, 104, 105, 106]
even = [r for r in selected if r % 2 == 0]
print("Even rolls         :", even)

# 14-15. Search (capital letters aur extra spaces ignore)
clean = lambda t: " ".join(t.split()).casefold()
data = {clean(c): {clean(s) for s in st} for c, st in courses.items()}
name = clean(input("Student name: "))
crs = clean(input("Course: "))
if crs not in data:
    print("Course not found")
elif name in data[crs]:
    print(f"YES, {name.title()} is registered for {crs.title()}")
else:
    print(f"NO, {name.title()} is NOT registered for {crs.title()}")

# 16. Final summary
print("\n--- FINAL SUMMARY ---")
print("Unique students :", len(everyone))
print("All three       :", sorted(all3))
print("Exactly one     :", sorted(one))
print("Roll range      :", rolls[0], "to", rolls[-1])
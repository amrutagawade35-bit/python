marks = {
    "Amit": 85,
    "Priya": 92,
    "Rahul": 78,
    "Sneha": 95
}
topper = max(marks, key=marks.get)
print("Topper =", topper)
print("Marks =", marks[topper])
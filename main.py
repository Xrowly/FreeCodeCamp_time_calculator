
from time_calculator import add_time

# Example test cases
test_cases = [
    ("11:59 PM", "24:05", None),
    ("3:00 PM", "3:10", None),
    ("11:30 AM", "2:45", "Monday"),
    ("8:15 PM", "12:00", "Wednesday"),
]

for start, duration, startday in test_cases:
    result = add_time(start, duration, startday)
    day_str = f", {startday}" if startday else ""
    print(f"{start} + {duration}{day_str} = {result}")

# Time Calculator

## Overview

This project is a Python-based time calculator developed as part of the **freeCodeCamp Scientific Computing with Python** curriculum, specifically for the "Time Calculator" project. The program takes a start time, duration, and optional starting day, then calculates the resulting time and day after adding the duration. It handles 12-hour clock formats (AM/PM), 24-hour periods, and day transitions, with optional day-of-the-week output. The project demonstrates string parsing, time arithmetic, and conditional logic, aligning with freeCodeCamp's focus on practical coding skills.

## Features

- **Time Addition**: Add a duration (hours and minutes) to a start time in 12-hour format (e.g., "3:00 PM").
- **AM/PM Handling**: Correctly processes AM/PM transitions and converts between 12-hour and 24-hour formats internally.
- **Day Tracking**: Calculates the number of days elapsed and, if provided, determines the new day of the week.
- **Formatted Output**: Returns the result in a clean format, including optional day-of-week and day-elapsed indicators (e.g., "next day" or "n days later").
- **Input Validation**: Assumes valid inputs as per the project requirements (e.g., times in "HH:MM AM/PM" format).

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/Xrowly/time-calculator.git
   ```
3. Navigate to the project directory:
   ```
   cd time-calculator
   ```
4. No external dependencies are required, as the project uses only standard Python libraries.

## Usage

1. Run the main script to see example usage:
   ```
   python main.py
   ```
2. The `main.py` script demonstrates adding various durations to start times, with and without a starting day.

### Example Output

Running `main.py` produces output like:

```
11:59 PM + 24:05 = 12:04 AM (2 days later)
3:00 PM + 3:10 = 6:10 PM
11:30 AM + 2:45, Monday = 2:15 PM, Monday
8:15 PM + 12:00, Wednesday = 8:15 AM, Thursday (next day)
```

### Customizing Time Calculations

Modify `main.py` to perform custom time calculations. Example:

```python
from time_calculator import add_time

result = add_time("3:00 PM", "3:10")
print(result)  # Output: 6:10 PM

result = add_time("11:30 AM", "2:45", "Monday")
print(result)  # Output: 2:15 PM, Monday
```

## Code Structure

- **time_calculator.py**: Contains the `add_time` function, which handles time arithmetic and formatting.
- **main.py**: Demonstrates usage with sample time calculations, showcasing the functionality required by the freeCodeCamp project.

## Limitations

- The application assumes valid input formats (e.g., "HH:MM AM/PM" for start time and "HH:MM" for duration).
- It is console-based and does not support persistent storage or graphical interfaces.
- Day-of-the-week input is case-insensitive but must match one of the seven days.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests that align with the freeCodeCamp Scientific Computing with Python curriculum goals. Ensure changes maintain the project's educational focus.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was completed as part of the **freeCodeCamp Scientific Computing with Python** curriculum, which emphasizes practical programming skills through hands-on projects. Visit [freeCodeCamp.org](https://www.freecodecamp.org/learn/scientific-computing-with-python/) for more details on the curriculum and other learning resources.
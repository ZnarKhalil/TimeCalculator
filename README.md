# Arithmetic Arranger

This repository is a solution for the [FreeCodeCamp Scientific Computing with Python - Time Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator) problem.
Write a function named add_time that takes in two required parameters and one optional parameter:


- **start (str):**
  - Start time in the 12-hour clock format (ending in AM or PM).

- **duration (str):**
  - Duration time indicating the number of hours and minutes.

- **day (str, optional):**
  - Starting day of the week, case insensitive.

## Functionality
The function adds the duration time to the start time and returns the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

### Examples

```python
from time_calculator import add_time

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## Testing

Unit tests are located in `test_module.py`. Tests run automatically when you hit the "run" button.
#Create Your Own Python Decorator
# Objective Create your own decorator function to measure the amount of seconds that a function takes to execute.
# Expected Output fast_function run speed: 0.33974480628967285s \n slow_function run speed: 2.9590742588043213s
# Calculating Time
# time.time() will return the current time in seconds since January 1, 1970, 00:00:00.

# Try running the starting code to see the current time printed.
# If you run the code after a while, you'll see a new time printed. e.g. first run:  1598524371.736911 second run:  1598524436.357875

# Given the above information, complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function().
# You will need to complete the speed_calc_decorator() function.

import time

def speed_calc_decorator(func):
    def wrapper_function():
        start_time = time.time()
        result = func()
        end_time = time.time()
        time_spent = end_time - start_time
        print(f"{func.__name__} run speed: {time_spent}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(100_000_000): # 100 millions operations
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(1_000_000_000): # 1 billion operations
        i * i


fast_function()
slow_function()
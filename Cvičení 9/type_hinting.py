
# Needed imports for type hints
from typing import List, Dict, Optional, Any

# Int returning an int
def square(x):
    return x * x

# List of floats returning an optional float
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Merge two dictionaries with any key and value type returning a dictionary with any key and value type
def merge_dicts(a, b):
    return {**a, **b}

# List of dictionaries with a str key and optional float value returning list of  optional floats (None or float)
def process_data(data):
    results = []
    for d in data:
        if d.get("value"):
            results.append(d["value"])
    return results
""" Module docstring. """
import random

def get_random_numbers(count):
   """Return a list of random numbers."""
   return list(random.randint(1, count))

def bubble_sort(numbers):
   """Bubble sort algorithm."""
   num_count = len(numbers)
   for i in range(num_count):
       for j in range(0, num_count - i - 1):
           if num_count[j] > num_count[j + 1]:
               num_count[j], num_count[j + 1] = num_count[j + 1], num_count[j]
   return numbers

random_numbers = get_random_numbers(100)
sorted_numbers = bubble_sort(random_numbers)
print(f"Random numbers: {random_numbers}")
print(f"Sorted numbers: {sorted_numbers}")

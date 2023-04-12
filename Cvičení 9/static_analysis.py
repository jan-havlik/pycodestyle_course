import random

def get_random_numbers(count):
    random_numbers = []
    for i in range(count):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

count = 10
random_numbers = get_random_numbers(count)
sorted_numbers = bubble_sort(random_numbers)
print(f"Random numbers: {random_numbers}")
print(f"Sorted numbers: {sorted_numbers}")

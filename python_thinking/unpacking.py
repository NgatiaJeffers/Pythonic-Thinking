"""
    Things to Remember
✦ Python has special syntax called unpacking for assigning multiple
    values in a single statement.
✦ Unpacking is generalized in Python and can be applied to any
    iterable, including many levels of iterables within iterables.
✦ Reduce visual noise and increase code clarity by using unpacking
    to avoid explicitly indexing into sequences.
"""

# Tuple
snack_calories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}
items = tuple(snack_calories.items())
print(items)

# Accessing values in tuples through numerical indexes:
item = ('Peanut butter', 'Jelly')
first = item[0]
second = item[1]
print(first, 'and', second)

# Less visual noise
# Accessing values in tuples throung Unpacking
item = ('Peanut butter', 'Jelly')
first, second = item # Unpacking
print(first, 'and', second)

# Use of typical syntax with indexes to swap values btwn two positions
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp
names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

# Unpacking in sorting algorithm
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1] # Swap

names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

# Typical syntax for loops, comprehensions and generator expressions
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} has {calories} calories')

# Unnpacking the above expression along with enumerate built-in func
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')
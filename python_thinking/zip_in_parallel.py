"""
    Things to Remember
✦ The zip built-in function can be used to iterate over multiple iterators in parallel.
✦ zip creates a lazy generator that produces tuples, so it can be used
    on infinitely long inputs.
✦ zip truncates its output silently to the shortest iterator if you supply
    it with iterators of different lengths.
✦ Use the zip_longest function from the itertools built-in module if you wan
"""

import itertools

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)

# Iterate over both lists in parellel
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

# Use of enumerate
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

# Clearer code using zip
# Zip -built-in func that wraps two or more iterators with a lazy generator
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

# If you don't expect the lengths of the lists passed to zip to be equal
# consider using the zip_longest func from the itertools
# built-in modules
names.append('Roselind')
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

# zip_longest replaces missing values--the length of the string 'Roslind'
# in this case--with whatever fillvalue is passed to it, which
# defaults to None.
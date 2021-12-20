"""
    Things to Remember
✦ Python's syntax makes it easy to write single-line expressions that
    are overly complicated and difficult to read.
✦ Move complex expressions into helper functions, especially if you
    need to use the same logic repeatedly.
✦ An if/else expression provides a more readable alternative to using
    the Boolean operators or and and in expressions.
"""

from urllib.parse import parse_qs

# Decoding a query string from a URL
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))

print('Red: ', my_values.get('red'))
print('Green: ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

# For query string 'red=5&blue=0&green='
# Helper function
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')

print(f'Red: {red!r}')
print(f'Green: {green!r}')
print(f'Opacity: {opacity!r}')
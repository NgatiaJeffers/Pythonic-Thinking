"""
    ✦ Avoid using else blocks after loops because their behavior isn't
    intuitive and can be confusing
"""

# Put else block immediately after a loop's repeated interior block:
for i in range(3):
    print('Loop', i)
else:
    print('Else block!')

# Using a break statement in a loop actually skips the else block:
for i in range(4):
    print('Loop', i)
    if i == 3:
        break
else:
    print('Else block')

# Runs immediately if you loop over an empty sequence:
for x in []:
    print('Never runs')
else:
    print('For Else block!')

# Determining whether two numbers are coprime
a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')

# Creating a helper function
# return early when I find the condition I'm looking for.
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4, 9)
assert not coprime(3, 6)

# Have a result variable that indicates whether I've found what I'm
# looking for in the loop. I break out of the loop as soon as I find something.
def coprime_alternate(a, b):
    is_comprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_comprime = False
            break
    return is_comprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)
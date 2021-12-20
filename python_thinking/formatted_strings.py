"""
    Things to Remember
✦ C-style format strings that use the % operator
    suffer from a variety of gotchas and verbosity problems.
✦ The str.format method introduces some useful concepts
    in its formatting specifiers mini language, but it
    otherwise repeats the mistakes of C-style format
    strings and should be avoided.
✦ F-strings are a new syntax for formatting values into
    strings that solves the biggest problems with
    C-style format strings.
✦ F-strings are succinct yet powerful because they allow
    for arbitrary Python expressions to be directly embedded
    within format 
"""


key = 'my_value'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)

f_string = f'{key:<10} = {value:.2f}'

c_tuple = '%-10s = %.2f' % (key, value)

str_args = '{:<10} = {:.2f}'.format(key, value)

str_kw = '{key:<10} = {value:.2f}'.format(key=key,
                                          value=value)
c_dict = '%(key)-10s = %(value).2f' % {'key': key,
                                        'value': value}
assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string
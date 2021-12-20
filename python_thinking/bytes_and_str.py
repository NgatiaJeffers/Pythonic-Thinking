# Unicode Sandwich - encoding and decoding of unicode data

# The function takes a byte or str instance and always returns a str:
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))

# The function takes a byte or str instance and always return a byte:
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
         value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))

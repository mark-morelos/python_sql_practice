'''
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:
- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0-9).
- It should only contain alphanumeric characters(a-z, A-Z & 0-9).
- No character should repeat.
- There must be exactly 10 characters in a valid UID.
'''

import re

# try - the  block lets you test a block of code for errors
# except - the block lets you handle the error
# assert - is used when debugging code, it lets you test if a condition in the code returns True


for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u) # must contain at least 2 uppercase English alphabet characters
        assert re.search(r'\d\d\d', u) # must contain at least 3 digits (0-9)
        assert not re.search(r'[^a-zA-Z0-9]', u) # should only contain alphanumeric characters(a-z, A-Z & 0-9)
        assert not re.search(r'(.)\1', u) #No character should repeat
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

# OTher solution:
    # u = input()
    # print('Valid' if all ([re.search(r, u) for r in [r'[A-Za-z0-9{10}', r'([A-Z].*){2}', r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', u) else 'Invalid')
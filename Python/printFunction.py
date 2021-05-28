'''
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
'''

n = 5

for i in range(1, n+1): # range defines 1 - given number (n) + 1 ie: n=5 : range (1,6)
    print (i, end="")
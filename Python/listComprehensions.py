'''
Let's learn about list comprehensions! You are given 3 integers x, y, and z representing the
dimensions of a cuboid along with integer n. Print a list of all possible coordinatess given by 
(i, j, k) on a 3d grid where the sum of i+j+k is not equal to n. 
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z.
Please use list comprehensions rather than multiple loops as a learning exercise.

Example:
x = 1
y = 1
z =2
n = 3

All permutations of [i,j,k] are:
[[0,0,0], [0,0,1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]

Print an array of the elements that do not sum to n = 3
'''

x = 1
y = 1
z =2
n = 3

print ([[a,b,c] for a in range (x+1) for b in range (y+1) for c in range (z+1) if a+b+c != n])
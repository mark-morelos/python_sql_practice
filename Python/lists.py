'''
Consider a list (list=[]). You can perform the following commands:
1. insert i e: Insert interger e at position i
2. print: Print the list
3. remove e: Delete the first occurrence of integer e
4. append e: Insert integer e at the end of the list
5. sort: Sort the list
6. pop: Pop the last element from the list
7. reverse: Reverse the list

Initialize your list and read in the value of n followed by n lines of commands where each
command will be of the 7 types listed above. Iterate through each command in order and perform 
the corresponding operation on your list.
'''

list = []
for _ in range(int(input())):
    command, *value = input().split()
    if command == 'print':
        print(list)
    else:
        getattr(list, command)(*(map(int, value)))

'''
the reason of * there is, it helps in passing the default value to the function so that the 
code can work.

The syntax of of getattr is :- getattr(Object,function)(vars)

As in this case our object is "L" and it doesn't contain the function passed in getattr, 
it will throw an error, so to avoid the error we are passing the default values of the function 
as mentioned in the question.

Like for the case (insert 0 5) it is like getattr(l,insert)(0,5). We are passing 0 and 5 to 
insert so that it will add 5 at the index 0 in the list.
'''
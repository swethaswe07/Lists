'''

Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
[1, 2, 3, 4]

'''

# Input the size of the list
n = int(input("Enter the size of the list: "))

# Initialize an empty list
my_list = []

# Input the elements of the list
for _ in range(n):
    element = int(input("Enter an element: "))
    my_list.append(element)

# Output the list
print(my_list)

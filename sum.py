'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11

'''

def sum_of_elements():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    
    # Check if n is within the allowed maximum
    if n > 20:
        print("Number of elements should not exceed 20.")
        return

    # Initialize a list to store the elements
    elements = []

    # Input the elements and append them to the list
    for _ in range(n):
        element = int(input())
        elements.append(element)

    # Calculate the sum of the elements
    total_sum = sum(elements)
    
    # Output the sum
    print(total_sum)

# Call the function
sum_of_elements()

'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 

'''

def print_reverse_list():
    # Input the list elements
    elements = input("Enter the list elements (space-separated): ").split()
    
    # Print the elements in reverse order
    reversed_elements = elements[::-1]
    
    # Output the reversed list as a space-separated string
    print(" ".join(reversed_elements))

# Call the function
print_reverse_list()

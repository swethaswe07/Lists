'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''

def sort_and_print_list():
    # Input the list elements
    elements = input("Enter the list elements (space-separated): ").split()
    
    # Convert the input strings to integers
    elements = [int(num) for num in elements]
    
    # Sort the list
    sorted_elements = sorted(elements)
    
    # Output the sorted list as a space-separated string
    print(" ".join(map(str, sorted_elements)))

# Call the function
sort_and_print_list()

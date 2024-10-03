'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3

'''

def count_value_repetitions():
    # Input the list elements
    elements = input("Enter the list elements (space-separated): ").split()
    
    # Convert the input strings to integers
    elements = [int(num) for num in elements]
    
    # Input the value to count
    value_to_count = int(input("Enter the value to count: "))
    
    # Count the occurrences of the value
    count = elements.count(value_to_count)
    
    # Output the count
    print(count)

# Call the function
count_value_repetitions()

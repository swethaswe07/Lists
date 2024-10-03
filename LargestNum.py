'''

Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6

'''

# Function to find the largest number in a list
def find_largest_number():
    # Input the size of the list
    size = int(input("Enter the size of the list: "))
    
    # Initialize an empty list
    numbers = []
    
    # Input the numbers and append them to the list
    for _ in range(size):
        num = int(input())
        numbers.append(num)
    
    # Find the largest number using the max function
    largest_number = max(numbers)
    
    # Output the largest number
    print(largest_number)

# Call the function
find_largest_number()

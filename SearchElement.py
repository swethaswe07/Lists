'''
Write a Program to find the search element in the given list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.
Third input consists of the element which we need to search
Sample Input 1:
5
1 2 3 6 5
3
Sample Output 1:
3 is present in the given list
Sample Input 2:
5
1 2 3 6 5
4
Sample Output 2:
4 is not present in the given list
'''

def find_smallest_number():
    # Input the size of the list
    size = int(input("Enter the size of the list: "))
    
    # Initialize an empty list
    numbers = []
    
    # Input the numbers and append them to the list
    for _ in range(size):
        num = int(input())
        numbers.append(num)
    
    # Find the smallest number using the min function
    smallest_number = min(numbers)
    
    # Output the smallest number
    print(smallest_number)

# Call the function
find_smallest_number()

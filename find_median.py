#Write a Python program to find the median of a list of numbers.
#Creating a function and parameter is numbers
def find_median(numbers):
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Find the middle index
    n = len(numbers)
    mid = n // 2

    # Check if the length of the list is odd or even
    if n % 2 == 0:
        # If even average two middle numbers
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        # If odd take the middle number
        median = numbers[mid]
    # return median 
    return median


numbers = [7, 1, 3, 4, 9, 2] 
# funtion calling
median_value = find_median(numbers) 
# displsy the median value
print(f"The median of the list is: {median_value}")

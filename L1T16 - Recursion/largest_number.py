# Define a recursive function 'largest_number' that takes an array as input.
def largest_number(array):
    # Base case: If the array has only one element, return that element as the largest number.
    if len(array) == 1:
        return array[0]

    # Get the first element from the list.
    num1 = array[0]
    # Recursively call 'largest_number' with the rest of the list.
    num2 = largest_number(array[1:])

    # Compare 'num1' and 'num2' to find the largest number.
    if num1 > num2:
        return num1
    else:
        return num2

# Call the 'largest_number' function with an example array and print the result.
result = largest_number([1, 2, 3, 4, 5])
# Print the result, which should be the largest number in the array.
print("Largest number: " + str(result))

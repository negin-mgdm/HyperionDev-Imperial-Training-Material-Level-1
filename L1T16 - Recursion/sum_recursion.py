# Define a recursive function called 'adding_up_to' that takes a list 'array' and an integer 'counter' as arguments.
def adding_up_to(array, counter):
    # Base case: If the 'counter' reaches -1, return 0.
    if counter == -1:
        return 0
    
    # Get the current value from the first element of the 'array'.
    current = array[0]
    
    # Create a new list 'new_array' containing all elements from 'array' except the first one.
    new_array = array[1:]
    # Recursively call 'adding_up_to' with the reduced 'new_array' and decremented 'counter'.
    add_up_to = adding_up_to(new_array, counter - 1)
    
    # Calculate the result by adding 'current' and 'add_up_to'.
    result = current + add_up_to
    return result

# Call the 'adding_up_to' function with the provided list and counter.    
result = adding_up_to([1,2,3,4,5], 3)

print("result: " + str(result))


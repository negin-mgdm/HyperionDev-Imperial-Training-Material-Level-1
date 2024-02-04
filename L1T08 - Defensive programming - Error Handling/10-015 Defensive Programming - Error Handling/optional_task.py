# Input desired numbers to calculate average (enter 0 to calculate average)

total = 0
count = 0

number = int(input("Please enter a number (enter 0 to exit):"))

while number != 0:
    total = number      # LogicalError, Should be total += number 
    count += 1
    number = int(input("Please enter a number (enter 0 to exit):"))
    
average = total/count       # LogicalError, Calculate average as a float

print ("The average is: " + average)       # RuntimeError, average should be str
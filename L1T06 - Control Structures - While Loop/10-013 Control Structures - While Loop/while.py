total = 0
count = 0

number = float(input("Please enter a number (enter -1 to exit):"))

while number != -1:
    total += number
    count += 1
    number = float(input("Please enter a number (enter -1 to exit):"))
    if number == -1:
        average = float(total/count)
        print ("The average is: ", average)
        break
    
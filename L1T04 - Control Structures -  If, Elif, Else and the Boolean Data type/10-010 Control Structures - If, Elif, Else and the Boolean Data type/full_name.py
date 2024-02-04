name = input("Please enter your full name:")    

name_length = len(name)     # Calculate the length of name characters and Store it in variable name_length

if name == (""):
    print("You haven't entered anything. Please enter your full name")
elif name_length < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif name_length > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")
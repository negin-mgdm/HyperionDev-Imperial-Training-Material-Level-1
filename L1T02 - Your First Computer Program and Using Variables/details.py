""" READ a string from user and store it in variable name
PRINT name
READ an integer from user and store it in variable age
PRINT age
READ an integer from user and store it in variable houseNo
PRINT houseNo
READ a string from user and store it in a variable street_name
PRINT street_name
READ gender from user and store it in variable gender
    IF gender is male
        PRINT This is + name. He is + age years old and lives at house number + houseNo on + street_name.
    ELIF gender is female
        PRINT This is + name. She is + age years old and lives at house number + houseNo on + street_name.
    ELSE 
        PRINT This is + name. They are + age years old and lives at house number + houseNo on + street_name."""


name = input("What is your name?")
print (name)
age = input("How old are you?")
print (age)
houseNo = input("What is your house number")
print (houseNo)
street_name = input("What is your street name?")
print (street_name)
gender = input("Are you male or female? ")
is_male = gender == "male"
is_female = gender == "female"

print("")

if is_male:
    print(f"This is {name}. He is {age} years old and lives at house number {houseNo} on {street_name}.")
elif is_female:
    print(f"This is {name}. She is {age} years old and lives at house number {houseNo} on {street_name}.")
else:
    print(f"This is {name}. They are {age} years old and live at house number {houseNo} on {street_name}.")



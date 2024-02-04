print ("Welcome to the error program")      # SyntaxError, Missing parentheses
print ("\n")        # SyntaxError, Missing parentheses

age_str = "24"    # RuntimeError, Removed years old as it cannot cast as int, Removed excess equal sign which was not applicable here
age = int(age_str)       # Unnecessary space
print("I'm " + str(age) + " years old.")       # RuntimeError, Read age as str

years_from_now = 3     # LogicalError, Removed double quotes around the "3" and Read 3 as an int
total_years = age + years_from_now
print ("The total number of years: " + str(total_years))       # SyntaxError, RuntimeError, Missing parentheses, Total was not defined, Read total_years as str instead

total_months = total_years * 12 + 6     # RuntimeError, LogicalError, Read total_years, Missing additional 6 months

print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old")      # SyntaxError, LogicalError, Missing parentheses, Read total_months as str


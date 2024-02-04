animal = "Lion"       # SyntaxError, Missing double quotes to create a string variable
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."      # LogicalError, Missing f-string formatting, Replacing number_of_teeth with animal_type 

print (full_spec)         # SyntaxError, Missing parentheses
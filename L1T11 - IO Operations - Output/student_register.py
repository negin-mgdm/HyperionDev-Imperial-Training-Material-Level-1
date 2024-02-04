# Ask the user to input the number of students
student_num = int(input("Please enter the number of students:"))
# Create an empty string to store student information
students = ""

# Loop to gather student ID for the specified number of students
for i in range(student_num):
    # Ask the user to input the student ID
    student_ID = input("Please enter student ID:")
    # Add the student ID to the 'students' string along with a dotted line 
    students = students + student_ID + ' .........' + '\n'
 
# Open a file named "reg_form.txt" and write the collected student ID to the file
with open("reg_form.text", "w") as file:
    file.write(students)

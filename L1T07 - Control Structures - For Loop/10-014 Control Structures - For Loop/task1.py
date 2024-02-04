total_row = 9  # Total number of rows

for row_num in range(1, total_row + 1):   
     
    if row_num <= 5 :     # Rows number 1 to 5
        num_stars = row_num
    
    else:
        num_stars = total_row - row_num + 1        # Rows number 6 to 9
        
    print('*' * num_stars)



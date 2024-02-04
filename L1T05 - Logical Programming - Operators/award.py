swimming = int(input("Please enter the swimming time in minutes:"))
cycling = int(input("Please enter the cycling time in minutes:"))
running = int(input("Please enter the running time in minutes:"))

total_time = swimming + cycling + running

if total_time == 100 or total_time < 100:
    print("Congratulations! You have finished within the the qualifying time and won Provincial Colours.")
elif total_time > 100 and total_time <= 105:
    print("You have finished within 5 minutes of qualifying time and won Provincial Half Colours.")
elif total_time > 100 and total_time <= 110:
    print("You have finished within 10 minutes of qualifying time and won Provincial Scroll.")
else:
    print("You have finished 10 minutes off from qualifying time. Keep practicing, and you'll knock it down next time!")
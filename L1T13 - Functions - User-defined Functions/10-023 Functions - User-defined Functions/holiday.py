# Define a function 'plane_cost' that calculates the cost of a plane ticket based on the destination city.
def plane_cost(city):
    city = city.title()
    if city == "London" :
        return 300
    elif city == "Paris" :
        return 220
    elif city == "Rome" :
        return 260
    elif city == "Barcelona":
        return 230    
 
# Request user input for the destination city.    
city_flight= input("Please enter the city you will be flying to (London, Paris, Rome, Barcelona): ")

# Check if the user input is in the list of valid cities.
valid_cities = ["London", "Paris", "Rome", "Barcelona"]
while not city_flight.title() in valid_cities:
    print("Selected city does not appear in the available options. Please choose from London, Paris, Rome, or Barcelona.")
    city_flight= input("Please enter the city you will be flying to (London, Paris, Rome, Barcelona): ")   
    
# Define a function 'hotel_cost' that multiplies the number of days and the cost of hotel per night.
def hotel_cost(days, cost_per_night=60):
    total = days * cost_per_night
    return (total)

# Request user input for the number of nights to stay at a hotel.
num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))

# Define a function 'car_rental' that multiplies the number of days and the cost of renting a car per day.    
def car_rental(days, rent_per_day=20):
        total = days * rent_per_day
        return (total)  

# Request user input for the number of days to hire a car.
rental_days = int(input("Please enter the number of days that you will be hiring a car: "))

# Define a function 'holiday_cost' that calculates the total cost of the holiday.
def holiday_cost(city_flight, num_nights, rental_days):
    total = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
    return total

# Calculate and print the cost of the plane ticket.    
plane_ticket_cost = plane_cost(city_flight)
print("Total Plane Cost: £" + str(plane_ticket_cost))    

# Calculate and print the total cost of hotel.
total_hotel_cost = hotel_cost(num_nights, cost_per_night=60)
print("Total Hotel Cost: £" + str(total_hotel_cost))

# Calculate and print the total cost of renting a car.
total_car_rental_cost = car_rental(rental_days, rent_per_day=20)
print("Total Car Rental Cost: £" + str(total_car_rental_cost))

# Calculate and print the total holiday cost.
total_cost = holiday_cost(city_flight, num_nights, rental_days)
print("Total Holiday Cost: £" + str(total_cost))












 





    
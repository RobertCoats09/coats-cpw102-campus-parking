# use a named constant
# automatically stored as float due to decimal
# available anywhere in program due to being defined at the top
COST_PER_HOUR = 2.0

def calculate_estimated_parking_cost(hours):
    estimated_cost = hours * COST_PER_HOUR
    return estimated_cost

# define the main logic of my program
def main():
    
    # create a variable to store the user's parked hours
    parked_hours = float(input("How many hours will/have you parked for? "))
    # call our function
    cost = calculate_estimated_parking_cost(parked_hours)

    # output
    print("Your parking cost will be/is $" + str(cost))

# call my main function and execute the logic of my program
main()
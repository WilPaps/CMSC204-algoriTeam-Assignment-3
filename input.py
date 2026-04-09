from data import locations

def get_starting_location():
    
    # Prompt user for starting point
    start_point = input("Enter starting point: ").strip().upper()
    
    # Validate input
    if start_point not in locations:
        print("Invalid location")
        print(f"Available locations: {', '.join(locations)}")
        exit()
    
    return start_point


def get_ending_location():
    
    # Prompt user for ending point
    end_point = input("Enter ending point: ").strip().upper()
    
    # Validate input
    if end_point not in locations:
        print("Invalid location")
        print(f"Available locations: {', '.join(locations)}")
        exit()
    
    return end_point

# Run the function when this file is executed directly
if __name__ == "__main__":
    starting_location = get_starting_location()
    print(f"You selected starting point: {starting_location}")
    
    ending_location = get_ending_location()
    print(f"You selected ending point: {ending_location}")
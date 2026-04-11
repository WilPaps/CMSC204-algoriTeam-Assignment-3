from data import locations, location_names

def display_locations():
    print("\n=== AVAILABLE LOCATIONS ===")
    for i, node in enumerate(locations, start=1):
        print(f"{i}. {location_names[node]}")


def get_location(prompt):
    while True:
        try:
            choice = int(input(prompt))

            if 1 <= choice <= len(locations):
                return locations[choice - 1]

            print("Invalid number. Try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")
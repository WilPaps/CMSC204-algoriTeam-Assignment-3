# main - compile everything here

from input import display_locations, get_location
from bfs import TransportGraph
from data import location_names


def menu():
    print("\n=== TRANSPORT SYSTEM ===")
    print("1. Find shortest route (fewest number of stops)")
    print("2. Exit")


def main():
    graph = TransportGraph()

    while True:
        menu()
        choice = input("Select option: ").strip()

        if choice == "1":

            display_locations()

            start = get_location("\nEnter starting point (number): ")
            end = get_location("Enter destination (number): ")

            if start == end:
                print("Start and destination cannot be the same.")
                continue

            print(f"\nFinding route from {location_names[start]} to {location_names[end]}...\n")

            graph.bfs(start, end)

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
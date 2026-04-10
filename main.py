# main - compile everything here
from input import get_starting_location, get_ending_location
from bfs import bfs, bfs_graph
from data import locations, graph

def display_welcome_message():
    print("=" * 60)
    print("    BREADTH-FIRST SEARCH")
    print("=" * 60)
    print(f"Available locations: {', '.join(locations)}")
    print("-" * 60)

def get_user_inputs():
    """Get starting and ending locations from user"""
    print("\n📍 LOCATION INPUT")
    print("-" * 20)
    
    starting_location = get_starting_location()
    print(f"Starting point selected: {starting_location}")
    
    ending_location = get_ending_location()
    print(f"Ending point selected: {ending_location}")
    
    return starting_location, ending_location

def run_bfs_analysis(start, end):
    """Run BFS and capture results"""
    print(f"\n🔍 RUNNING BFS FROM {start} TO {end}")
    print("=" * 60)
    
    # Run the BFS algorithm
    bfs(bfs_graph, start, end)

def display_summary(start, end):
    """Display a summary of the pathfinding session"""
    print("\n" + "=" * 60)
    print("    SESSION SUMMARY")
    print("=" * 60)
    print(f"Start Location: {start}")
    print(f"Target Location: {end}")
    print(f"Total Locations Available: {len(locations)}")
    print("=" * 60)

def main():
    """Main function that consolidates all operations"""
    try:
        # Display welcome message
        display_welcome_message()
        
        # Get user inputs
        start, end = get_user_inputs()
        
        # Display summary before analysis
        display_summary(start, end)
        
        # Run BFS analysis
        run_bfs_analysis(start, end)
        
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
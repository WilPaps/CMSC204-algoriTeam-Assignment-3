# Location list from the graph
locations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] #modify with real locations

# Graph represented as an adjacency list (dictionary)
graph = {
    "A": ["B", "E"],
    "B": ["A", "F", "I", "J"],
    "C": ["D", "E"],
    "D": ["C", "F"],
    "E": ["A", "C", "H"],
    "F": ["B", "D", "H"],
    "G": ["H", "I", "J"],
    "H": ["E", "F", "G", "J"],
    "I": ["B", "G", "J"],
    "J": ["B", "G", "H", "I"]
}
import heapq

# Define the Node class
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  # Heuristic value

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.h < other.h

def best_first_search(maze, start, end):
    # Create start and end nodes
    start_node = Node(start, None)
    end_node = Node(end, None)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Defining possible movements: right, left, up, down
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node (node with smallest heuristic value)
        #Heappop returns the smallest item from the heap. We use this to find the node with the smallest heuristic value).
        #Smallest item can also be used by doing heap[0] to index it because a heap organizes from smallest to largest. 
        current_node = heapq.heappop(open_list)

        # Add the current node to the closed list
        closed_list.append(current_node)

        # Found the goal: reconstruct and return the path
        # If the current node is the goal, we've found a path. 
        # We then reconstruct this path from the goal to the start by following the parent pointers and return the path.
        if current_node == end_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            #[::-1] reverses the values in the list so it goes from start to end and not end to start. 
            return path[::-1] # Return reversed path

        # Generate children
        # Explore neighbors: For each of the four directions, we get the position of the neighboring node. 
        # If this position is within the maze, and is not a wall, we create a new node for this position.
        for movement in movements: 
            # Position of potential child
            child_position = (current_node.position[0] + movement[0], current_node.position[1] + movement[1])

            # Check if position is within the maze
            if (child_position[0] < 0 or child_position[0] >= len(maze) or 
                child_position[1] < 0 or child_position[1] >= len(maze[0])):
                continue

            # Check if the position is walkable
            if maze[child_position[0]][child_position[1]] != 0:
                continue

            # Create new node
            # Takes the node it was just exploring adjacent tiles from and makes it the parent node and creates a new node for the child
            # Position that is related to that parent node. This makes the process reversible as shown above. 
            # The child node is then added to the list of nodes which need to be restored and they'll be searched in the next iteration.
            # The algorithm will then continue to generate and examine neighbours until it either finds a path or doesn't. 
            child_node = Node(child_position, current_node)

            # Child node is on the closed_list
            if child_node in closed_list:
                continue

            # Find the heuristic value h for the child node
            child_node.h = abs(child_position[0] - end_node.position[0]) + abs(child_position[1] - end_node.position[1])

            # Child node is already in the open_list
            if child_node in open_list:
                continue

            # Add the child node to the open_list
            heapq.heappush(open_list, child_node)

    # If the end can't be reached, return None
    # Once there are no new neighbours or nodes to search the loop is complete, if a path is not found the loop ends and returns None. 
    return None

maze = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
start = (0, 14)
end = (19, 12)
print(best_first_search(maze, start, end))

import heapq
from test_algorithms.heuristics import manhattan
from test_algorithms.informed_helpers import get_neighbors, path_travelled

# Greedy Best First Search is an informed search algorithm that finds 
# the quickest path from one point to another, in this case, 
# the snake's head to the food.
# It only considers how far it estimates it still needs to go 
# to reach the food, and completely ignores how far it has already traveled. 
# This makes it a faster algorithm, but one which can be vulnerable to hitting 
# dead ends or taking a longer route overall.

# For this algorithm, we use the heapq Python library to implement a priority queue.
# A normal list is not ordered by priority, so this library allows us to easily 
# retrieve the smallest value, or here, the most promising cell at each 
# step without extra overhead.

def informed_greedy_bfs(
    pos_h: tuple,
    pos_f: tuple,
    body: list,
    cell_number: int
    ) -> list:

    # unexplored_frontier is a priority queue holding cells that have been 
    # discovered but not yet explored.
    # known_cell_map is a dictionary recording how we reached each cell on the grid.
    unexplored_frontier: list = []
    known_cell_map: dict = {pos_h: None}

    # manh_cost is the initial Manhattan heuristic estimate from the head to the food.
    manh_cost = manhattan(pos_h, pos_f)
    heapq.heappush(unexplored_frontier, (manh_cost, pos_h))

    while unexplored_frontier:
        current_h, current_loc = heapq.heappop(unexplored_frontier)

        if current_loc == pos_f:
            return path_travelled(known_cell_map, current_loc)

        for neighbor in get_neighbors(current_loc, cell_number, body):
            if neighbor not in known_cell_map:
                known_cell_map[neighbor] = current_loc
                new_f = manhattan(neighbor, pos_f)
                heapq.heappush(unexplored_frontier, (new_f, neighbor))

    return []
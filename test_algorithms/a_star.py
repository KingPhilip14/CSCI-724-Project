import heapq

from test_algorithms.heuristics import manhattan
from test_algorithms.informed_helpers import get_neighbors, path_travelled

# A* is an informed search algorithm that finds the optimal path from one point 
# to another, in this case, the snake's head to the food. 
# It works by exploring the most promising cells first, balancing how far it has 
# already traveled from the start, and how far it estimates it still needs to go 
# to reach the food. This ensures that A* always finds the shortest possible path 
# without exploring unnecessary cells.

# For this algorithm, we use the heapq Python library to implement a priority queue.
# A normal list is not ordered by priority, so this library allows us to easily 
# retrieve the smallest value, or here, the most promising cell at each 
# step without extra overhead.

def informed_a_star(
    pos_h: tuple,
    pos_f: tuple,
    body: list,
    cell_number: int
    ) -> list:

    # unexplored_frontier is a priority queue holding cells that have been 
    # discovered but not yet explored.
    # cost_so_far is a dictionary tracking the lowest known cost to reach each cell.
    # known_cell_map is a dictionary recording how we reached each cell on the grid.
    unexplored_frontier: list = []
    cost_so_far: dict = {pos_h: 0}
    known_cell_map: dict = {pos_h: None}

    # manh_cost is the initial Manhattan heuristic estimate from the head to the food.
    manh_cost = manhattan(pos_h, pos_f)
    heapq.heappush(unexplored_frontier, (manh_cost, pos_h))

    while unexplored_frontier:
        current_f, current_loc = heapq.heappop(unexplored_frontier)

        if current_loc == pos_f:
            return path_travelled(known_cell_map, current_loc)

        for neighbor in get_neighbors(current_loc, cell_number, body):
            new_cost = cost_so_far[current_loc] + 1

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                known_cell_map[neighbor] = current_loc
                new_f = new_cost + manhattan(neighbor, pos_f)
                heapq.heappush(unexplored_frontier, (new_f, neighbor))

    return []
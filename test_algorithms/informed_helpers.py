def path_travelled(known_cell_map, current_loc) -> list:
    """
    The path_travelled function traces back the path taken by the snake to reach its current location.

    Starting from the current location, we follow the known_cell_map backwards,
    adding each location to the list until we reach the start where the value is None.
    The list is then reversed to give us the path from the head to the food.
    """
    path = []
    while current_loc is not None:
        path.append(current_loc)
        current_loc = known_cell_map[current_loc]
    path.reverse()
    return path


def get_neighbors(current_loc, cell_number, body) -> list:
    """
    The get_neighbors function checks the four possible directions of movement 
    from the current location of the head, and returns a listr of valid neighboring cells.

    If the space is blocked by the snake's body, or out of bounds (i.e it will collide witht he wall), 
    we do not consider it a possible neighbor. 
    It returns a list of valid neighboring positions that the snake can move to from its 
    current location.

    To note; the tail is position is not considered as an invalid cell as it should be 
    moving forward as the sanke moves.
    """
    blocked = set(body[:-1])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    neighbors = []
    
    for direction in directions:
        neighbor = (current_loc[0] + direction[0], current_loc[1] + direction[1])
        within_bounds = 0 <= neighbor[0] < cell_number and 0 <= neighbor[1] < cell_number
        not_blocked = neighbor not in blocked

        if within_bounds and not_blocked:
            neighbors.append(neighbor)
    
    return neighbors
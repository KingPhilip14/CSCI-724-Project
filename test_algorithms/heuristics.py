def manhattan(pos_h, pos_f) -> int:
    """
    We are using the Manhattan distance as our choice of heuristic here.

    Briefly, according to GeeksForGeeks, the Manhattan distance measures 
    how far apart two points are by summing the absolute differences of 
    their coordinates. It is especially useful along grid-like paths, where 
    movement is restricted to horizontal and vertical directions.

    In our snake game, there are only four possible directions to move at 
    any given time barring any obstacles; left, right, up, down. As such 
    this heuristic works for us. 
    
    It measures the difference in x and y coordinates between the head 
    and the food, giving us a reliable distance estimate that never 
    overshoots the actual distance.
    """
    return abs(pos_f[0] - pos_h[0]) + abs(pos_f[1] - pos_h[1])
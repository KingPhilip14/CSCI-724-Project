# import pygame to use the Vector2 class
from pygame import Vector2

class BFSPathfinder:
    
    def __init__(self, board_size):
        """
        Inputs:
               - The Board Size
        """
        pass
        
    def find_next_move(self, head, fruit, body, current_direction):
        """
        Inputs:
               - head: represents the head of the snake.
               - fruit: the apple the snake is heading towards.
               - body: the body of the snake.
               - current_direction: the snake-bound direction.
        
        Output:
               - return the current_direction
        """
        pass
    
    def get_neighbors(self, cell):
        """
        Input:
             - Cell: Represents a a grid where the sbnake can move or the other pieces
             like the game tiles are placed.
        Output:
             - Returns a list of the directions (x, y - 1),  # up (x, y + 1),  # down (x - 1, y),  # left, (x + 1, y)
        """
        pass
        
    
    def is_valid_cell(self, cell, blocked):
        """
        Input:
              - Cell: Represents a a grid where the sbnake can move or the other pieces
             like the game tiles are placed.
              - Blocked: checks if the next cell is blocked. 
        Output: 
              - returns if the snake if is inside the board and the next cell is not blocked.
        """
        pass 
    
    def rebuild_path(self, parent, start, goal):
        """
        Input:
              - parent:
              - start:
              - goal:
        """
        pass
    
    def cell_to_direction(self, head, next_cell):
        """
        Input:
              - head:
              - next_cell:
        """
        pass 
    
    def vector_to_tuple(self, position):
        """
        Input:
              - position:
        """
        pass
        
        
# import pygame to use the Vector2 class
from pygame import Vector2
from collections import deque
import typing 
class BFSPathfinder:
    
    def __init__(self, board_size: int):
        """
        Inputs:
               - The Board Size
        """
        self.board_size = board_size
        
    def is_reverse_move(self, start: tuple[int, int], neighbor: tuple[int, int], current_direction: Vector2) -> bool:
        move_x = neighbor[0] - start[0]
        move_y = neighbor[1] - start[1]
        
        next_direction = (move_x, move_y)
        
        reverse_direction = (-int(current_direction.x), -int(current_direction.y))
        
        return next_direction == reverse_direction
        
    def find_next_move(self, head: Vector2, fruit: Vector2, body: list[Vector2], current_direction: Vector2) -> Vector2:
        """
        Inputs:
               - head: represents the head of the snake.
               - fruit: the apple the snake is heading towards.
               - body: the body of the snake.
               - current_direction: the snake-bound direction.
        
        Output:
               - return the current_direction
        """
        start = self.vector_to_tuple(head)
        goal = self.vector_to_tuple(fruit)
        blocked = {self.vector_to_tuple(block) for block in body[1:]}
        
        queue: deque[tuple[int, int]] = deque([start])
        visited: set[tuple[int, int]] = {start}
        parent: dict = {}
        found_goal: bool = False 
        
        while queue:
            current = queue.popleft()
            
            if current == goal:
                found_goal = True 
                break
                
            for neighbor in self.get_neighbors(current):
                if current == start and self.is_reverse_move(start, neighbor, current_direction):
                    continue
                
                if neighbor not in visited and self.is_valid_cell(neighbor, blocked):
                    visited.add(neighbor)
                    parent[neighbor] = current 
                    queue.append(neighbor)
                    
        if found_goal:
            path = self.rebuild_path(parent, start, goal)
            
            if len(path) > 1:
                next_cell = path[1]
                return self.cell_to_direction(start, next_cell)
        # BFS Logic
        return current_direction
    
    
    def get_neighbors(self, cell: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Input:
             - Cell: Represents a a grid where the sbnake can move or the other pieces
             like the game tiles are placed.
        Output:
             - Returns a list of the directions (x, y - 1),  # up (x, y + 1),  # down (x - 1, y),  # left, (x + 1, y)
        """
        x , y = cell
        
        # next return the directions
        return [
            (x, y - 1), # up
            (x, y + 1), # down
            (x - 1, y), #left
            (x + 1, y)  # right
        ]
        
    
    def is_valid_cell(self, cell: tuple[int, int], blocked: set[tuple[int, int]]) -> bool:
        """
        Input:
              - Cell: Represents a a grid where the sbnake can move or the other pieces
             like the game tiles are placed.
              - Blocked: checks if the next cell is blocked. 
        Output: 
              - returns if the snake if is inside the board and the next cell is not blocked.
        """
        x, y = cell
        
        inside_board = 0<= x < self.board_size and 0 <= y < self.board_size
        not_blocked = cell not in blocked
        
        return inside_board and not_blocked
    
    def rebuild_path(self, parent: dict[tuple[int, int], tuple[int, int]], start: tuple[int, int], goal: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Input:
              - parent:
              - start:
              - goal:
        """
        path: list[tuple[int, int]] = [goal]
        current: tuple[int, int] = goal 
        
        while current != start:
            current = parent[current]
            path.append(current)
            
        path.reverse()
        return path
    
    def cell_to_direction(self, head: tuple[int, int], next_cell: tuple[int, int]) -> Vector2:
        """
        Input:
              - head:
              - next_cell:
        """
        head_x, head_y = head 
        next_x, next_y = next_cell 
        
        if next_x == head_x and next_y == head_y - 1:
            return Vector2(0, -1)
        if next_x == head_x and next_y == head_y + 1:
            return Vector2(0, 1)
        if next_x == head_x - 1 and next_y == head_y:
            return Vector2(-1, 0)
        if next_x == head_x + 1 and next_y == head_y:
            return Vector2(1, 0)
        
        return Vector2(0,0)
    
    def vector_to_tuple(self, position: Vector2) -> tuple[int, int]:
        """
        Input:
              - position:
        """
        return int(position.x), int(position.y)
    
        
        
from pygame.math import Vector2
from config import CELL_NUMBER
from search.bfs import BFSPathfinder
from search.dijkstra import DijkstraPathfinder

bfs = BFSPathfinder(CELL_NUMBER)
dijkstra = DijkstraPathfinder(CELL_NUMBER)

def bfs_bridge(pos_h, pos_f, body, cell_number):
    head = Vector2(pos_h[0], pos_h[1])
    fruit = Vector2(pos_f[0], pos_f[1])
    body_vec = [Vector2(b[0], b[1]) for b in body]
    direction = bfs.find_next_move(head, fruit, body_vec, Vector2(0, 0))
    return [pos_h, (pos_h[0] + int(direction.x), pos_h[1] + int(direction.y))]

def dijkstra_bridge(pos_h, pos_f, body, cell_number):
    head = Vector2(pos_h[0], pos_h[1])
    fruit = Vector2(pos_f[0], pos_f[1])
    body_vec = [Vector2(b[0], b[1]) for b in body]
    direction = dijkstra.find_next_move(head, fruit, body_vec, Vector2(0, 0))
    return [pos_h, (pos_h[0] + int(direction.x), pos_h[1] + int(direction.y))]
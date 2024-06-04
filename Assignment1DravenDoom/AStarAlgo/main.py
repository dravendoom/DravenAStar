import pygame
import math
import lines
from queue import PriorityQueue

import lines
from nodesystem import Node
from grid import Grid
from utility import Util

def main():

    pygame.init()
    screen = pygame.display.set_mode((500, 250))
    grid = Grid(50, 25)

    #Setting Start and End Nodes in grid
    grid.set_start(2, 20, True)
    grid.set_end(47, 3, True)

    #Setting Active Nodes
    grid.set_corner(6, 17, True, "A")
    grid.set_corner(6, 24, True, "B")
    grid.set_corner(23, 24, True, "C")
    grid.set_corner(23, 17, True, "D")
    grid.set_corner(6, 13, True, "E")
    grid.set_corner(11, 14, True, "F")
    grid.set_corner(13, 8, True, "G")
    grid.set_corner(10, 4, True, "H")
    grid.set_corner(4, 8, True, "I")
    grid.set_corner(14, 14, True, "J")
    grid.set_corner(20, 14, True, "K")
    grid.set_corner(17, 7, True, "L")
    grid.set_corner(20, 9, True, "M")
    grid.set_corner(21, 3, True, "N")
    grid.set_corner(25, 2, True, "O")
    grid.set_corner(27, 5, True, "P")
    grid.set_corner(24, 12, True, "Q")
    grid.set_corner(27, 19, True, "R")
    grid.set_corner(31, 16, True, "S")
    grid.set_corner(30, 12, True, "T")
    grid.set_corner(36, 12, True, "U")
    grid.set_corner(36, 2, True, "V")
    grid.set_corner(30, 2, True, "W")
    grid.set_corner(35, 16, True, "X")
    grid.set_corner(33, 18, True, "Y")
    grid.set_corner(33, 22, True, "Z")
    grid.set_corner(35, 24, True, "1")
    grid.set_corner(41, 24, True, "2")
    grid.set_corner(43, 22, True, "3")
    grid.set_corner(43, 18, True, "4")
    grid.set_corner(41, 16, True, "5")
    grid.set_corner(44, 14, True, "6")
    grid.set_corner(39, 5, True, "7")
    grid.set_corner(42, 3, True, "8")
    grid.set_corner(45, 5, True, "9")

    #manually adding neighbors to each node
    Util.add_neighbor_to_node_by_name(grid, "START", ("A", "B", "E", "I"))
    Util.add_neighbor_to_node_by_name(grid, "A", ("B", "D", "E", "F", "I", "J", "K", "START"))
    Util.add_neighbor_to_node_by_name(grid, "B", ("A", "C", "E", "I", "1", "2", "START"))
    Util.add_neighbor_to_node_by_name(grid, "C", ("B", "D", "R", "Q", "S", "Y", "X", "Z", "1", "2", "U"))
    Util.add_neighbor_to_node_by_name(grid, "D", ("C", "A", "K", "J", "L", "F", "Q", "R", "Z", "1", "M"))
    Util.add_neighbor_to_node_by_name(grid, "E", ("F", "I", "A", "START", "B"))
    Util.add_neighbor_to_node_by_name(grid, "F", ("E", "G", "J", "L", "N", "K", "A", "D"))
    Util.add_neighbor_to_node_by_name(grid, "G", ("F", "H", "L", "J", "N"))
    Util.add_neighbor_to_node_by_name(grid, "H", ("G", "I", "L", "N", "D"))
    Util.add_neighbor_to_node_by_name(grid, "I", ("E", "H", "A", "START", "B"))
    Util.add_neighbor_to_node_by_name(grid, "J", ("F", "L", "G", "K", "D", "A"))
    Util.add_neighbor_to_node_by_name(grid, "K", ("J", "F", "A", "L", "M", "P", "Q", "R", "D"))
    Util.add_neighbor_to_node_by_name(grid, "L", ("G", "F", "H", "J", "K", "M", "N", "L", "D", "R"))
    Util.add_neighbor_to_node_by_name(grid, "M", ("L", "N", "P", "Q", "T", "K", "D", "R", "S", "X"))
    Util.add_neighbor_to_node_by_name(grid, "N", ("O", "L", "G", "H", "F"))
    Util.add_neighbor_to_node_by_name(grid, "O", ("W", "V", "P", "N", "H"))
    Util.add_neighbor_to_node_by_name(grid, "P", ("O", "M", "W", "T", "Q", "K", "S"))
    Util.add_neighbor_to_node_by_name(grid, "Q", ("R", "S", "D", "C", "K", "M", "P", "T", "W", "X", "5", "U", "6"))
    Util.add_neighbor_to_node_by_name(grid, "R", ("Q", "S", "M", "K", "D", "C", "L", "2", "1", "Y", "X", "U"))
    Util.add_neighbor_to_node_by_name(grid, "S", ("R", "Q", "M", "P", "T", "U", "6", "X", "Y", "5", "Z", "C"))
    Util.add_neighbor_to_node_by_name(grid, "T", ("U", "6", "5", "X", "Y", "S", "Q", "M", "P", "W"))
    Util.add_neighbor_to_node_by_name(grid, "U", ("6", "5", "X", "Y", "S", "Q", "V", "T", "7"))
    Util.add_neighbor_to_node_by_name(grid, "V", ("END", "8", "7", "6", "5", "4", "U", "W", "Q"))
    Util.add_neighbor_to_node_by_name(grid, "W", ("V", "T", "Q", "P", "O"))
    Util.add_neighbor_to_node_by_name(grid, "X", ("U", "7", "6", "5", "Y", "R", "S", "C", "Q", "T"))
    Util.add_neighbor_to_node_by_name(grid, "Y", ("U", "X", "Z", "C", "R", "S", "T"))
    Util.add_neighbor_to_node_by_name(grid, "Z", ("Y", "1", "C", "D", "R", "S"))
    Util.add_neighbor_to_node_by_name(grid, "1", ("2", "C", "D", "R", "B"))
    Util.add_neighbor_to_node_by_name(grid, "2", ("3", "1", "C", "B"))
    Util.add_neighbor_to_node_by_name(grid, "3", ("4", "6", "9", "END", "2"))
    Util.add_neighbor_to_node_by_name(grid, "4", ("6", "END", "3", "5", "V", "7"))
    Util.add_neighbor_to_node_by_name(grid, "5", ("6", "4", "X", "S", "Q", "T", "U", "V", "7"))
    Util.add_neighbor_to_node_by_name(grid, "6", ("9", "END", "B", "4", "5", "X", "S", "Q", "T", "U", "V", "7"))
    Util.add_neighbor_to_node_by_name(grid, "7", ("8", "6", "4", "5", "X", "U", "V"))
    Util.add_neighbor_to_node_by_name(grid, "8", ("END", "9", "7", "V"))
    Util.add_neighbor_to_node_by_name(grid, "9", ("END", "6", "3", "8"))
    Util.add_neighbor_to_node_by_name(grid, "END", ("V", "8", "9", "6", "4", "3"))

    #Gathering Hueristic Value for all Nodes/Vertices
    Util.loop_all_vertices(grid)
    #Astar returning reverse path
    path = Util.astaralgo(grid)
    grid.draw(screen)
    lines.draw_line_list(screen)
    Util.draw_reverse_path(grid, screen, path)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()
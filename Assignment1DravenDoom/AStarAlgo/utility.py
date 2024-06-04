import pygame
import math
import lines
from queue import PriorityQueue


class Util:
    def draw_reverse_path(grid, screen, path):
        if path is not None:
            for i in range(len(path) - 1):
                start_pos = (path[i].x * 10, path[i].y * 10 + 5)
                end_pos = (path[i + 1].x * 10, path[i + 1].y * 10 + 5)
                pygame.draw.line(screen, (184, 45, 82), start_pos, end_pos, 2)

    def get_node_at_coordinate(grid, x, y):
        for row in grid.grid:
            for node in row:
                if node.x == x and node.y == y:
                    return node
        return None

    def find_end_node(grid):
        for row in grid.grid:
            for node in row:
                if node.end:
                    print("END NODES HEXCODE:",  node)
                    return node

    def loop_all_vertices(grid):
        endnode = Util.find_end_node(grid)
        x2 = endnode.x
        y2 = endnode.y
        for row in grid.grid:
            for node in row:
                if node.corner:
                    x1 = node.x
                    y1 = node.y
                    node.h = Util.get_euclids_dist(grid, x1, y1, x2, y2)
                    print("Hueristic distance:", node.h)

    def get_euclids_dist(grid, x1, y1, x2, y2):
        one = math.pow((x2-x1), 2)
        two = math.pow((y2-y1), 2)
        ans = one + two
        ans = math.sqrt(ans)
        return ans

    def get_node_by_name(grid, id):
        for row in grid.grid:
            for node in row:
                if node.identifier == id:
                    if id == "START":
                        print("THIS IS THE START NODE:", node)
                    return node
        return None

    def add_neighbor_to_node(grid, x, y, neighbor_x, neighbor_y):
        node = Util.get_node_at_coordinate(grid, x, y)
        neighbor = Util.get_node_at_coordinate(grid, neighbor_x, neighbor_y)
        if node and neighbor:
            print(neighbor.x, neighbor.y)
            node.set_neighbor(neighbor)

    def add_neighbor_to_node_by_name(grid, id1, idList):
        node = Util.get_node_by_name(grid, id1)
        i = 0
        for ids in idList:
            neighbor = Util.get_node_by_name(grid, idList[i])
            node.set_neighbor(neighbor)
            i = i + 1

    def return_neighbors(grid, id):
        neighbor_list = []
        node = Util.get_node_by_name(grid, id)
        x = node.x
        print(x)
        y = node.y
        print(y)
        print(node.neighbors)
        if node:
            for neighbors in node.neighbors:
                neighx = neighbors.x
                neighy = neighbors.y
                localDist = Util.get_euclids_dist(grid, x, y, neighx, neighy)
                neighbor_list.append(neighbors)
        return neighbor_list

    def astaralgo(grid):
        #DECLARATIONS
        oq = PriorityQueue()
        cl = []
        start = Util.get_node_by_name(grid, "START")
        end = Util.find_end_node(grid)

        #INITIAL STATE
        start.h = Util.get_euclids_dist(grid, start.x, start.y, end.x, end.y)
        oq.put((start.f, start))

        while not oq.empty():
            cur = oq.get()[1]
            print("----------------- CURRENT NODE: ", cur.identifier, " ------------------\n")
            cl.append(cur)
            for nodes in list(oq.queue):
                print(nodes[0], nodes[1].identifier)
            if cur == end:
                return Util.End_Node_Reached_Return_Path(grid, cur, start)
            for neighbor in cur.neighbors:
                if neighbor not in oq.queue and neighbor not in cl:
                    g = cur.g + Util.get_euclids_dist(grid, cur.x, cur.y, neighbor.x, neighbor.y)
                    if neighbor not in oq.queue or g < neighbor.g:
                       Util.Solve_neighbors_func_val(grid, neighbor, cur, oq, g, start, end)

        return None

    def Solve_neighbors_func_val(grid, neighbor, cur, oq, g, start, end):
        print("---------------- NEIGHBOR: ", neighbor.identifier, " ------------------")
        neighbor.g = g
        print("Neighbor's hVal: ", neighbor.h)

        neighbor.distance = Util.get_euclids_dist(grid, cur.x, cur.y, neighbor.x, neighbor.y)
        print("Neighbor's gVal: ", neighbor.g, "( ", cur.g, "+", neighbor.distance, " )")
        print("Neighbor's local Distance: ", neighbor.distance)
        neighbor.parent = cur
        neighbor.f = neighbor.g + neighbor.h
        print("Neighbor's fVal: ", neighbor.f)
        oq.put((neighbor.f, neighbor))


    def End_Node_Reached_Return_Path(grid, cur, start):
        path = []
        while cur != start:
            path.append(cur)
            cur = cur.parent
        path.append(start)
        return list(reversed(path))
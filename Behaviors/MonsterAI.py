from definitions import *
from queue import Queue

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.row == other.row and self.col == other.col
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "(" + str(self.row) + ", "  + str(self.col) + ")"


class MonsterAI:
    def __init__(self, dungeon_map):
        self.dungeon_map = dungeon_map


    def solve(self, monster, player): #BFS. Pulled form my C++ code from PPW homework 1
        #create queue
        q = Queue()
        start = Position(monster.row, monster.col)
        q.put(start)

        #create a visited array
        visited = []

        for row in range(0, ROW_COUNT):
            visited.append([])
            for col in range(0, COLUMN_COUNT):
                visited[row].append(False)

        visited[monster.row][monster.col] = True

        #prev array filled with None for nulls
        prev = []
        for row in range(0, ROW_COUNT):
            prev.append([])
            for col in range(0, COLUMN_COUNT):
                prev[row].append(None)

        while(not q.empty()):
            p = q.get()

            #get valid moves
            neighbors = []
            for i in [UP, DOWN, LEFT, RIGHT]:
                if self.dungeon_map.get_tile_type(p.row+i[0], p.col+i[1]) == FLOOR: #the spot next to the current spot is a floor
                    neighbors.append(Position(p.row+i[0], p.col+i[1]))

            for current_neighbor in neighbors:
                if not visited[current_neighbor.row][current_neighbor.col]:
                    q.put(current_neighbor)
                    visited[current_neighbor.row][current_neighbor.col] = True
                    prev[current_neighbor.row][current_neighbor.col] = p
        return prev


    def reconstruct_path(self, monster, player, prev):
        # print("in reconstruct path")
        start = Position(monster.row, monster.col)
        end = Position(player.row, player.col)
        path = []

        # follow the path back from end to start
        current_position = end
        while(current_position != None):
            path.append(current_position)
            current_position = prev[current_position.row][current_position.col]
        path.reverse()

        if path[0] == start: #if there was a path
            return path
        else:
            return []

    def next_move(self, monster, player):
        prev = self.solve(monster, player)
        path = self.reconstruct_path(monster, player, prev)
        player_position = Position(player.row, player.col)

        if(not path == []): # if there is a path to the player
            if(not player_position == path[0] and not player_position == path[1]): #if the monster is not right next to the player
                return path[1]
        #the monster shouldn't try to move since it's either trapped or next to the player.
        return path[0]

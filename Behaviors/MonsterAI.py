from definitions import *
from queue import Queue

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class MonsterAI:
    def __init__(self, dungeon_map):
        self.dungeon_map = dungeon_map


    def solve(self, monster, player):
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
            print(p.row, p.col)

            #get valid moves
            neighbors = []
            for i in [UP, DOWN, LEFT, RIGHT]:
                if self.dungeon_map.get_tile_type(p.row+i[0], p.col+i[1]) == FLOOR: #the spot next to the current spot is a floor
                    neighbors.append(Position(p.row+i[0], p.col+i[1]))
                    print("Valid neighbor is at: ", p.row+i[0], p.col+i[1])

            for current_neighbor in neighbors:
                if not visited[current_neighbor.row][current_neighbor.col]:
                    q.put(current_neighbor)
                    visited[current_neighbor.row][current_neighbor.col] = True
                    print("checking prev at: ", current_neighbor.row, current_neighbor.col)
                    prev[current_neighbor.row][current_neighbor.col] = p

        return prev


    def reconstruct_path(monster, player, prev):
        pass

    def next_move(monster, player):
        pass


# std::vector<std::vector<Position>> Pathfinder::solve(Position start, Position end){
#   // create q
#   std::queue<Position> q;
#   q.push(start);
#
#   // initialize visited array with all falses
#   bool visited[board_->get_rows()][board_->get_cols()];
#
#   for(int i = 0; i<board_->get_rows(); i++){
#     for(int j = 0; j<board_->get_cols(); j++){
#       visited[i][j] = false;
#     }
#   }
#   visited[start.row][start.col] = true;
#
#   // 2d vector of Positions
#   std::vector<std::vector<Position>> prev;
#
#   // initialize to (-1, -1) as a null value
#   prev.resize(board_->get_rows(), std::vector<Position>(board_->get_cols()));
#   for(int i = 0; i < board_->get_rows(); i++){
#     for(int j = 0; j < board_->get_cols(); j++){
#       prev[i][j] = Position(-1, -1);
#     }
#   }
#
#   while(!q.empty()){
#     Position p = q.front();
#     q.pop();
#
#     // temporary player to use GetMoves
#     Player * player = new Player("default", true);
#     player->SetPosition(p);
#     std::vector<Position> neighbors = board_->GetMoves(player);
#
#     //
#     for(unsigned int i = 0; i< neighbors.size(); i++){
#       Position current_neighbor = neighbors[i];
#       if(!visited[current_neighbor.row][current_neighbor.col]){
#         // add the neighbor to queue, set it as visited, and set it's prev position
#         q.push(current_neighbor);
#         visited[current_neighbor.row][current_neighbor.col] = true;
#         prev[current_neighbor.row][current_neighbor.col] = p;
#       }
#     }
#   }
#   return prev;
# }

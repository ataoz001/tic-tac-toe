from tic_tac_toe import *

welcome_screen = "Welcome to the tic-tac-toe CLI game"


class Player:
    def __init__(self, name, id, tile):
        self.name = name
        self.score = 0
        self.id = id
        self.tile = tile
        self.tileLocs = []


"""

"""


# (1,1) , (1,2), 1,3), (2,1) (2 , 2) , (2 , 3), (3,1) , (3,2) , (3, 3)
class Board:
    def __init__(self):
        self.ui = """
                        1   2   3
                      ____ ____ ____ 
                    1| {} | {} | {} |  
                     |____|____|____|
                    2| {} | {} | {} |
                     |____|____|____|
                    3| {} | {} | {} |
                     |____|____|____|
                      
         
        """
        self.matrix = [". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]

    def update_matrix(self, player, matrix, input):
        if input[0] == "1":
            if input[2] == "1":
                if matrix[0] == ". ":
                    matrix[0] = player.tile
            elif input[2] == "2":
                if matrix[1] == ". ":
                    matrix[1] = player.tile
            elif input[2] == "3":
                if matrix[2] == ". ":
                    matrix[2] = player.tile

        elif input[0] == "2":
            if input[2] == "1":
                if matrix[3] == ". ":
                    matrix[3] = player.tile
            elif input[2] == "2":
                if matrix[4] == ". ":
                    matrix[4] = player.tile
            elif input[2] == "3":
                if matrix[5] == ". ":
                    matrix[5] = player.tile

        elif input[0] == "3":
            if input[2] == "1":
                if matrix[6] == ". ":
                    matrix[6] = player.tile
            elif input[2] == "2":
                if matrix[7] == ". ":
                    matrix[7] = player.tile
            elif input[2] == "3":
                if matrix[8] == ". ":
                    matrix[8] = player.tile
        print(matrix)
        return matrix

    def update_ui(self, string, current_board_matrix):
        cbm = current_board_matrix
        string = string.format(
            cbm[0], cbm[1], cbm[2], cbm[3], cbm[4], cbm[5], cbm[6], cbm[7], cbm[8]
        )
        return string


def main():
    board = Board()
    game_turns = 0
    print(welcome_screen)
    firt_player_name = input("What is the first player's name: ")
    player1 = Player(firt_player_name, 0, "X ")
    second_player_name = input("What is the second player's name: ")
    player2 = Player(second_player_name, 1, "O ")
    flag = True
    print(board.update_ui(board.ui, board.matrix))
    while flag:
        if game_turns % 2 == 0:
            print(f"It's your turn {player1.name}")
            move = input("enter your move: ")
            tile_loc = tuple(move)
            player1.tileLocs.append(tile_loc)
            temp = [x for x in board.matrix]
            board.update_matrix(player1, board.matrix, move)
            if temp == board.matrix:
                print(
                    "You have entered a tile that was already filled\nPlease select another one."
                )

            else:
                a = board.update_ui(board.ui, board.matrix)
                print("Move successful!")
                print(a)
                game_turns += 1

        else:
            print(f"It's your turn {player2.name}")
            move = input("enter your move: ")
            tile_loc = tuple(move)
            player2.tileLocs.append(tile_loc)
            temp = [x for x in board.matrix]
            board.update_matrix(player2, board.matrix, move)
            if temp == board.matrix:
                print(
                    "You have entered a tile that was already filled\n Please select another one."
                )

            else:
                a = board.update_ui(board.ui, board.matrix)
                print(a)
                game_turns += 1

        if game_turns == 8:
            print("game is over")
            flag = False


main()

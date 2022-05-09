

class Tic_Tac_Toe():

    class resources():
        def __init__(self):
            self.clean_board = \
"""
___|___|___
___|___|___
   |   |  
"""
            self.board_key = \
"""
_ul_|_um_|_ur_
_ml_|_mm_|_mr_
 bl | bm | br 
"""
            self.board_index = {"ul":2, "um":6, "ur":10, "ml":14, "mm":18, "mr":22, "bl":26, "bm":30, "br":34}
            self.board_matrix = [["ul", "um", "ur"], ["ml", "mm", "mr"], ["bl", "bm", "br"]]
            self.players = ["x", "o"] 
            self.opening_text = "TIC TAC TOE"

    def __init__(self):
        self.resources = self.resources()
        self.game_board = self.resources.clean_board
        self.board_index = self.resources.board_index
        self.board_matrix = self.resources.board_matrix
        self.moves_played = 0
        self.players = self.resources.players
        self.opening_text = self.resources.opening_text
        self.to_play = 0
    
    def play_move(self, player:str, pos:str):
        try:
            pos_index = self.board_index[pos]
        except KeyError:
            raise Exception("Invalid Position")
            return 
        if self.game_board[pos_index] in ["o", "x"]:
            raise Exception("Position Occupied")
            return 
        self.game_board = self.game_board[:pos_index] + player + self.game_board[pos_index+1:]

    def prompt_move(self, player:str):
        print(f"It is \"{player}\"\'s move!")
        while True:
            try:
                print(f"(to see valid positions type '!help'")
                pos = input("Where would you like to place? ")
                if pos == "!help":
                    print("The position names are:")
                    print(self.resources.board_key)
                else:
                    self.play_move(player, pos)
                    return 
            except Exception as e:
                print(e)
                continue
    
    def check_for_win(self, player):
        check_row = []
        check_col = []
        for i in range(3): 
            for j in range(3):
                check_row.append(self.board_matrix[i][j])
                check_col.append(self.board_matrix[j][i])
            row_occupied_by_player = [self.game_board[self.board_index[x]] == player for x in check_row]
            col_occupied_by_player = [self.game_board[self.board_index[x]] == player for x in check_col]
            won = all(row_occupied_by_player) or all(col_occupied_by_player)
            if won:
                return True
            check_row, check_col = [], []
        return False


    def play(self):
        replay = True
        print(self.opening_text)
        input("PRESS ENTER TO PLAY")
        print(self.game_board)
        while replay:
            player_move = self.players[self.to_play]
            self.prompt_move(player_move)
            print(self.game_board)
            self.to_play = 0 if self.to_play else 1
            if self.check_for_win(player_move):
                print(f"\"{self.players[self.to_play]}\" WON!!")
                while replay:
                    play_again = input("Would you like to play again (Y/N)? ")
                    if play_again in ["Y", "N"]:
                        if play_again == "N":
                            replay = False
                        if play_again == "Y":
                            replay = True
                            self.to_play = 0
                            break
                    else: 
                        print("Invalid Input - Enter \"Y\" for yes or \"N\" for no")
                        replay = True 
                        continue
        print("Thanks For Playing!!!")
                    
    
    def replay() -> bool:
        pass


if __name__ == "__main__":
    game = Tic_Tac_Toe() 
    game.play()
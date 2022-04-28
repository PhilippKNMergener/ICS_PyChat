

class tic_tac_toe():

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
        return

    def prompt_move(self, player:str):
        while True:
            try:
                print(f"It is \"{player}\"\'s move!")
                print(f"(to see valid positions type '!help'")
                pos = input("Where would you like to place? ")
                if pos == "!help":
                    print("The position names are:")
                    print(self.resources.board_key)
                    continue
                else:
                    self.play_move(player, pos)
            except Exception as e:
                print(e)
                continue
            break
    
    def check_for_win(self, player):
        pass

    def play(self):
        print(self.opening_text)
        input("PRESS ENTER TO PLAY")
        while True:
            player_move = self.players[self.to_play]
            print(self.game_board)
            self.prompt_move(player_move)
            self.to_play = 0 if self.to_play else 1
            if self.check_for_win(player_move):
                print(f"\"{self.players[player_move]}\" WON!!")
                replay = True
                while replay:
                    play_again = input("Would you like to play again (Y/N)? ")
                    if play_again in ["Y", "N"]:
                        if play_again == "N":
                            replay = False
                        if play_again == "Y":
                            replay = True
                            break
                    else: 
                        print("Invalid Input - Enter \"Y\" for yes or \"N\" for no")
                        replay = True 
                        continue
    
    def replay() -> bool:
        pass


if __name__ == "__main__":
    game = tic_tac_toe() 
    game.play()
clean_board = """
___|___|___
___|___|___
   |   |  
"""
board_index = {"ul":2, "um":6, "ur":10, "ml":14, "mm":18, "mr":22, "bl":26, "bm":30, "br":34}
board_matrix = [["ul", "um", "ur"], ["ml", "mm", "mr"], ["bl", "bm", "br"]]
for pos in board_index.values():
    print(clean_board[pos])
print(pos for row in board_matrix for pos in row)
class tic_tac_toe():
    def init():
        pass
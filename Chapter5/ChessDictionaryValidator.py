''' valid if:
1. exactly one black king and exactly one white king
2. Each player can only have at most 16 pieces
3. at most 8 pawns per player
4. all pieces must be on a valid space from '1a' to '8h'
5. The piece names begin with either a 'w' or 'b' to represent white or black
6.  -> followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

'''


defaults = {'1a': '','2a': '', '3a': '','4a': '','5a': '','6a': '','7a': '','8a': '', '1b': '','2b': '', '3b': '','4b': '','5b': '','6b': '','7b': '','8b': '', '1c': '','2c': '', '3c': '','4c': '','5c': '','6c': '','7c': '','8c': '', '1d': '','2d': '', '3d': '','4d': '','5d': '','6d': '','7d': '','8d': '', '1e': '','2e': '', '3e': '','4e': '','5e': '','6e': '','7e': '','8e': '', '1f': '','2f': '', '3f': '','4f': '','5f': '','6f': '','7f': '','8f': '', '1g': '','2g': '', '3g': '','4g': '','5g': '','6g': '','7g': '','8g': '', '1h': '','2h': '', '3h': '','4h': '','5h': '','6h': '','7h': '','8h': ''}

board1={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn'}
board2={'1h': 'bking', '6c': 'queen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'pawn'}
board3={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn', '3c': 'wking'}
board4={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn', '3c': 'wpawn', '9z': 'wpawn'}
board5={'1h': 'bking', '6c': 'wqueln', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn'}

rightvalues = { 'bking': 'bking', 'bqueen': 'bqueen', 'bbishop': 'bbishop', 'bpawn': 'bpawn', 'bknight': 'bknight', 'brook': 'brook', 'wking': 'wking', 'wqueen': 'wqueen', 'wbishop': 'wbishop', 'wpawn': 'wpawn', 'wknight': 'wknight', 'wrook': 'wrook' }



def isValidChessBoard(board):
    bc = 0 #counter
    wc = 0 #counter
    defaults.update(board)


    if str(board).count('wking') == 1 and str(board).count('bking') == 1: # check for exactly 1 king on both sides [1]
        for j in board.values(): # check for only black or white pieces [5]
            if j[0] == 'b':
                bc += 1
            elif j[0] == 'w':
                    wc += 1
            elif j[0] != 'b' or j[0] != 'w':
                return False
        if bc > 16 and wc > 16: # check for max 16 pieces per side [2]
            return False
        
        for k in board.values(): #check if only correct pieces are on the board [6]
            if k in rightvalues.keys():
                continue
            else :
                print("invalid board (pieces are not correct)")
                return False

        if str(board).count('bpawn') > 8 or str(board).count('wpawn') > 8: #check for max 8 pawns on both sides [3]
            return False

        if len(defaults.keys()) != 64: #check for valid space 1a to 8h [4]
            return False

        return True
    else:
        return False



print(bool(isValidChessBoard(board1)))
